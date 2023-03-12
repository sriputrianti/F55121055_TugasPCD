import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
img = cv2.imread('kopi.jpg', 0)

# Compute the FFT of the image
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Define the radius of the low-pass filter in pixels
radius = 50

# Create a circular mask to apply the low-pass filter
rows, cols = img.shape
crow, ccol = rows//2, cols//2
mask = np.zeros((rows, cols), np.uint8)
cv2.circle(mask, (ccol, crow), radius, 255, -1)

# Apply the mask to the shifted FFT
fshift_filtered = fshift * mask

# Shift the zero-frequency component back to the top-left corner
f_filtered = np.fft.ifftshift(fshift_filtered)

# Compute the inverse FFT to obtain the filtered image
img_filtered = np.fft.ifft2(f_filtered)
img_filtered = np.abs(img_filtered)

# Display the original and filtered images
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_filtered, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
