import numpy as np
import cv2
import pygame
from pygame import mixer

# Initialize pygame for sound
pygame.init()
mixer.init()

# Load the alarm sound
try:
    alarm = mixer.Sound('music.mp3')  # Replace with the correct path
except pygame.error as e:
    print(f"Error loading sound: {e}")
    alarm = None  # Prevent crashing if sound fails

# Start video capture
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 5, 1, 1)  # Noise reduction
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw face rectangle
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

            if len(eyes) >= 2:
                cv2.putText(frame, "Eyes open!", (100, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
                count = 0  # Reset blink count if eyes are open
                if alarm:
                    alarm.stop()
            else:
                print("Blink detected--------------")
                count += 1
                if count >= 10:  # Trigger alarm after 10 blinks
                    cv2.putText(frame, "Wake up\
                    s!", (100, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                    if alarm:
                        alarm.play()
    else:
        cv2.putText(frame, "No face detected", (100, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):  # Exit the loop when 's' is pressed
        break

cap.release()
cv2.destroyAllWindows()
