import cv2
import numpy as np

# Create a blank black image
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw a green rectangle
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw a blue circle
cv2.circle(image, (350, 250), 80, (255, 0, 0), 3)

# Draw a red line
cv2.line(image, (0, 0), (500, 500), (0, 0, 255), 2)

# Display image
cv2.imshow("Shapes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()