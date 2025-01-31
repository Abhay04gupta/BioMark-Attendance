from flask import Flask, render_template, Response, jsonify
import cv2
import os
import time
from ultralytics import YOLO
from deepface import DeepFace
from pathlib import Path

app = Flask(__name__)

# Load YOLO model for face detection
model = YOLO("yolov8n-face.pt")

# Create directories if they don’t exist
save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

# Attendance record (Predefined names)
attendance = { "Abhay": 0, "Rajveer": 0, "Aditya Chauhan": 0, "Aditya Yadav": 0, "Mayur": 0, "Saksham": 0 }

# Initialize video capture
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Convert frame to JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        # Yield frame for Flask response
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html', attendance=attendance)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    success, frame = cap.read()
    if not success:
        return jsonify({"status": "error", "message": "Failed to capture image"})

    img_index = len(os.listdir(save_dir))
    image_path = os.path.join(save_dir, f"captured_image{img_index}.jpg")
    cv2.imwrite(image_path, frame)

    # Face detection
    results = model.predict(source=frame, conf=0.5)
    bbox_list = results[0].boxes.xyxy.tolist()

    for i, bbox in enumerate(bbox_list):
        x1, y1, x2, y2 = map(int, bbox)
        face_crop = frame[y1:y2, x1:x2]

        # Save cropped face
        face_path = os.path.join(save_dir, f"face{i}.jpg")
        cv2.imwrite(face_path, face_crop)

        try:
            # Face recognition with DeepFace
            result = DeepFace.find(img_path=face_path, db_path="database", model_name="VGG-Face", enforce_detection=False)

            if result and len(result[0]["identity"]) > 0:
                file_path = Path(result[0]["identity"][0])
                recognized_name = file_path.parent.name
            else:
                recognized_name = "Unknown"
        except Exception as e:
            recognized_name = ""

        if recognized_name in attendance:
            attendance[recognized_name] = 1
            
    # Cleanup captured images
    for file in os.listdir(save_dir):
        file_path = os.path.join(save_dir, file)
        os.remove(file_path)
        
    return jsonify({"status": "success", "message": "Face detected", "attendance": attendance})

@app.route('/reset_attendance', methods=['POST'])
def reset_attendance():
    for name in attendance:
        attendance[name] = 0
    return jsonify({"status": "success", "message": "Attendance reset", "attendance": attendance})

if __name__ == "__main__":
    app.run(debug=True)
