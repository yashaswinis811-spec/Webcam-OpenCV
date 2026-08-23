import cv2

# Open video file
cap = cv2.VideoCapture("video.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Unable to open video.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video.")
            break

        cv2.imshow("Video Player", frame)

        # Press Q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()