import cv2

# Read image
image = cv2.imread("image.jpg")

# Resize image
resized = cv2.resize(image, (500, 400))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()