import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))

if not cap.isOpened():
    print("Error: Cannot access webcam.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save frame to video
        out.write(frame)

        cv2.imshow("Recording Video", frame)

        # Press Q to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved as output.mp4")