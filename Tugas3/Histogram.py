import cv2
from matplotlib import pyplot as plt

# Load an image
img = cv2.imread('Mawar.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Plot the histogram
plt.hist(gray.ravel(), 256, [0, 256])
cv2.imshow('Mawar', gray)
plt.show()
