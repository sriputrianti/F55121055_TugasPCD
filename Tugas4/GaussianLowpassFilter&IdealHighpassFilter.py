import numpy as np
import cv2
from matplotlib import pyplot as plt

def gaussian_lpfilter(rows, cols, sigma):
    mask = np.zeros((rows, cols), np.uint8)
    crow, ccol = rows//2, cols//2
    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i-crow)**2 + (j-ccol)**2)
            mask[i, j] = np.exp(-(d**2) / (2 * sigma**2))
    return mask

def ideal_hpfilter(rows, cols, radius):
    mask = np.ones((rows, cols), np.uint8)
    crow, ccol = rows//2, cols//2
    for i in range(rows):
        for j in range(cols):
            if np.sqrt((i-crow)**2 + (j-ccol)**2) <= radius:
                mask[i, j] = 0
    return mask

# Baca gambar
img = cv2.imread('k.jpg', 0)

# Lakukan transformasi Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Buat Gaussian Lowpass Filter
rows, cols = img.shape
mask_gaussian = gaussian_lpfilter(rows, cols, 50)

# Buat Ideal Highpass Filter
mask_ideal = ideal_hpfilter(rows, cols, 50)

# Aplikasikan filter pada gambar dalam domain frekuensi
fshift_gaussian = fshift * mask_gaussian
fshift_ideal = fshift * mask_ideal

# Kembalikan gambar ke domain spasial
f_ishift_gaussian = np.fft.ifftshift(fshift_gaussian)
img_back_gaussian = np.fft.ifft2(f_ishift_gaussian)
img_back_gaussian = np.abs(img_back_gaussian)

f_ishift_ideal = np.fft.ifftshift(fshift_ideal)
img_back_ideal = np.fft.ifft2(f_ishift_ideal)
img_back_ideal = np.abs(img_back_ideal)

# Tampilkan gambar hasil
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img_back_gaussian, cmap = 'gray')
plt.title('Gaussian LPF'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_back_ideal, cmap = 'gray')
plt.title('Ideal HPF'), plt.xticks([]), plt.yticks([])
plt.show()
