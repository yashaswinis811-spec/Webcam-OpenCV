import cv2

# Read image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Original Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()