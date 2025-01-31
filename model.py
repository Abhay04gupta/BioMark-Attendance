import cv2
from ultralytics import YOLO
from deepface import DeepFace
from pathlib import Path
import os
import time

# Load YOLO model for face detection
model = YOLO("yolov8n-face.pt")

# Create a directory to save cropped face images
save_dir = "captured_images"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Recognized faces
attendance = {"Abhay": 0, "Rajveer": 0, "Aditya Chauhan": 0, "Aditya Yadav": 0, "Mayur": 0, "Saksham": 0}

# Start video capture
cap = cv2.VideoCapture(0)  # 0 for webcam, or provide a video file path

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Show the frame
    cv2.imshow("Real-Time Face Detection", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        # Capture image
        img_index = len(os.listdir(save_dir))
        image_path = os.path.join(save_dir, f"captured_image{img_index}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Image captured at {image_path}")

        # Face Detection with YOLO
        results = model.predict(source=frame, conf=0.5)
        bbox_list = results[0].boxes.xyxy.tolist()

        for i, bbox in enumerate(bbox_list):
            x1, y1, x2, y2 = map(int, bbox)
            face_crop = frame[y1:y2, x1:x2]

            # Save cropped face
            face_path = os.path.join(save_dir, f"face{i}.jpg")
            cv2.imwrite(face_path, face_crop)

            try:
                # Use DeepFace for face recognition
                result = DeepFace.find(img_path=face_path, db_path="database", model_name="VGG-Face", enforce_detection=False)

                if result and len(result[0]["identity"]) > 0:
                    file_path = Path(result[0]["identity"][0])
                    recognized_name = file_path.parent.name
                else:
                    recognized_name = "Unknown"
            except Exception as e:
                print(f"DeepFace error: {e}")
                recognized_name = ""

            if recognized_name in attendance:
                attendance[recognized_name] = 1

            # Display bounding box and name
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 1)
            cv2.putText(frame, recognized_name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)

        # Show the processed frame with detections
        cv2.imshow("Processed Face Detection", frame)

        # Add small delay to reduce lag
        time.sleep(0.5)

    elif key == ord('e'):
        break

# Release the video capture object and close OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Cleanup captured images
for file in os.listdir(save_dir):
    file_path = os.path.join(save_dir, file)
    os.remove(file_path)

print(attendance)
