# 🚗 Drowsiness Detection System

## Overview
A real-time driver drowsiness detection system developed using Python, OpenCV, and Dlib. The system monitors eye movements through a webcam and triggers an alarm when signs of drowsiness are detected.

## Features
- Real-time webcam monitoring
- Facial landmark detection
- Eye Aspect Ratio (EAR) calculation
- Alarm on prolonged eye closure
- Easy to run

## Tech Stack
- Python
- OpenCV
- Dlib
- NumPy
- SciPy
- imutils

## Project Structure
## 📁 Project Structure

```
Drowsiness-Detection-System/
│── main.py                     # Main application
│── a.py                        # Eye detection module
│── aa.py                       # Alarm module
│── shape_predictor_68_face_landmarks.dat
│── music.mp3                   # Alarm sound
│── requirements.txt
│── README.md
│── LICENSE
```

## Installation
## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yash6912/Drowsiness-Detection-System.git
```

### Navigate to the project

```bash
cd Drowsiness-Detection-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run
## ▶️ How to Run

Run the following command:

```bash
python main.py
```

After launching the application:

- Allow webcam access.
- The system starts monitoring the driver's eyes.
- If prolonged eye closure is detected, an alarm sound is triggered automatically.

## Screenshots
![Screenshot](images/Images.png)


## Future Improvements
## 🚀 Future Improvements

- Improve detection accuracy under low-light conditions.
- Replace Dlib with MediaPipe for faster performance.
- Develop a mobile application.
- Integrate GPS to send emergency alerts.
- Store driver fatigue history for analysis.
- Deploy the system on embedded hardware like Raspberry Pi.

## Contributors
## 👥 Contributors

This project was developed as a four-member academic team.

**My Contributions:**

- Implemented and tested facial landmark detection.
- Assisted in integrating the Eye Aspect Ratio (EAR) algorithm.
- Performed debugging and testing.
- Managed GitHub repository updates.
