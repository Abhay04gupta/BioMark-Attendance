# Face Recognition Attendance System

## 📌 Overview
The **Face Recognition Attendance System** is a web-based application that utilizes facial recognition technology to automate attendance tracking. It captures images from a live video stream, detects faces, and marks attendance in real time.

## 🎯 Features
- 📷 **Live Camera Feed**: Displays real-time video feed for face recognition.
- 🏷️ **Face Detection**: Detects faces and verifies identities.
- ✅ **Automated Attendance Marking**: Marks users as **Present** or **Absent**.
- 📝 **Attendance Record**: Displays recorded attendance on the UI.
- 🎨 **Modern UI**: Dark-themed responsive interface.

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: OpenCV, dlib
- **Database**: SQLite / CSV for storing attendance

## 🚀 Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Abhay04gupta/BioMark-Attendance.git
   cd BioMark-Attendance
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**
   ```bash
   python app.py
   ```
5. **Access the Web App**
   Open your browser and go to `http://127.0.0.1:5000/`

## 📸 Usage
1. Start the server and access the web app.
2. The camera will display a **live feed**.
3. Click the **Capture** button to record attendance.
4. The system will detect faces and mark attendance.
5. Check attendance records in the **right panel**.
6. Click **Reset** to clear the attendance log.

## 🏗️ Project Structure
```
BioMark-Attendance/
│-- static/
│   ├── styles.css
│-- templates/
│   ├── index.html
│-- app.py
│-- requirements.txt
│-- README.md
```

## 📌 To-Do / Future Enhancements
- 🔹 Implement **face recognition using deep learning**.
- 🔹 Integrate **database for storing past attendance records**.
- 🔹 Add **user authentication** for secured access.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repo, make changes, and submit a pull request.

## 📜 License
This project is licensed under the **MIT License**.

---
💡 **Developed by [Abhay Gupta](https://github.com/Abhay04gupta)**

