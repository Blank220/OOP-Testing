import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize mediapipe face mesh for eye detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the screen size
screen_width, screen_height = pyautogui.size()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (MediaPipe uses RGB, OpenCV uses BGR)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get face landmarks
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get the coordinates of the left and right eyes (using landmarks 33 and 263)
            left_eye = face_landmarks.landmark[33]  # Left eye center (approximated)
            right_eye = face_landmarks.landmark[263]  # Right eye center (approximated)
            
            # Convert the landmarks to pixel coordinates
            h, w, _ = frame.shape
            left_eye_x, left_eye_y = int(left_eye.x * w), int(left_eye.y * h)
            right_eye_x, right_eye_y = int(right_eye.x * w), int(right_eye.y * h)

            # Calculate the center of both eyes
            eye_center_x = (left_eye_x + right_eye_x) // 2
            eye_center_y = (left_eye_y + right_eye_y) // 2

            # Normalize the eye position to screen coordinates
            screen_x = np.interp(eye_center_x, [0, w], [0, screen_width])
            screen_y = np.interp(eye_center_y, [0, h], [0, screen_height])

            # Move the cursor based on eye position
            pyautogui.moveTo(screen_x, screen_y)

            # Optional: Draw circles around the eyes and the center for visualization
            cv2.circle(frame, (left_eye_x, left_eye_y), 3, (0, 255, 0), -1)
            cv2.circle(frame, (right_eye_x, right_eye_y), 3, (0, 255, 0), -1)
            cv2.circle(frame, (eye_center_x, eye_center_y), 5, (0, 0, 255), -1)

    # Display the frame with visual feedback
    cv2.imshow("Eye Tracker", frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()