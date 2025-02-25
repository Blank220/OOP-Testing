import cv2

cap = cv2.VideoCapture(0)

# Initialize the first frame for comparison
ret, first_frame = cap.read()
first_frame = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(first_frame, gray)

    # Apply threshold to detect motion
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

    # Find contours (motion areas)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If motion is detected, save an image
    if len(contours) > 0:
        cv2.imwrite('motion_detected.jpg', frame)
        print("Motion detected! Image saved.")

    # Display the video feed
    cv2.imshow('Motion Detection', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
