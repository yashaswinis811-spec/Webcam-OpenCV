import cv2

# Open the default webcam (0)
camera = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    # Read a frame from the webcam
    ret, frame = camera.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Display the frame
    cv2.imshow("Webcam", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
camera.release()
cv2.destroyAllWindows()