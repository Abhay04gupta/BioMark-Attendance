# BioMark-Attendance

## Overview
BioMark-Attendance is a real-time face recognition-based attendance system that uses YOLO for face detection and DeepFace for face recognition. The system captures live video from a webcam, detects faces, recognizes predefined individuals, and marks attendance accordingly.

## Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript (Jinja templates)
- **Machine Learning Models:**
  - YOLO (for face detection)
  - DeepFace (for face recognition)
- **Libraries & Dependencies:**
  - OpenCV (cv2) for image processing
  - Ultralytics YOLO for face detection
  - DeepFace for facial recognition

## Features
- **Live Face Detection:** Uses YOLO to detect faces in real time.
- **Face Recognition:** Matches detected faces with stored identities using DeepFace.
- **Attendance Marking:** Updates attendance status when a recognized face is detected.
- **Automatic Image Capture & Cleanup:** Saves detected faces temporarily and removes them after processing.
- **Reset Attendance:** Allows resetting of attendance records.

## Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/Abhay04gupta/BioMark-Attendance.git
cd BioMark-Attendance
```

### 2. Create a Virtual Environment
```sh
python -m venv myenv
source myenv/bin/activate  # On Windows, use: myenv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Download YOLO Face Detection Model
Download the `yolov8n-face.pt` model and place it in the project directory.

### 5. Run the Application
```sh
python app.py
```

### 6. Open in Browser
Visit `http://127.0.0.1:5000/` to access the web application.

## Folder Structure
```
BioMark-Attendance/
│── captured_images/    # Temporarily stores detected faces
│── database/           # Stores reference images for face recognition
│── templates/
│   └── index.html      # Frontend UI
│── app.py              # Flask backend
│── requirements.txt    # Python dependencies
│── yolov8n-face.pt     # YOLO face detection model
```

## Future Improvements
- Enhance accuracy by fine-tuning DeepFace models.
- Add support for multiple users and database integration.
- Implement a web-based dashboard for attendance reports.
- Improve UI/UX with modern frontend frameworks.

## Contributors
- **Abhay Gupta** - [GitHub](https://github.com/Abhay04gupta)

## License
This project is open-source and available under the [MIT License](LICENSE).

