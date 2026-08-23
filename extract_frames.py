import cv2

# Open video file
cap = cv2.VideoCapture("video.mp4")

count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Save each frame as an image
    cv2.imwrite(f"frame_{count}.jpg", frame)
    count += 1

cap.release()

print(f"{count} frames extracted successfully.")