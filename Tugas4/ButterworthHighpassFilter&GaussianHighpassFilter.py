import numpy as np
import cv2
from matplotlib import pyplot as plt

def butterworth_hpfilter(rows, cols, radius, order):
    mask = np.zeros((rows, cols), np.uint8)
    crow, ccol = rows//2, cols//2
    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i-crow)**2 + (j-ccol)**2)
            if d != 0:
                mask[i, j] = 1 / (1 + (radius/d)**(2*order))
    return mask

def gaussian_hpfilter(rows, cols, sigma):
    mask = np.zeros((rows, cols), np.uint8)
    crow, ccol = rows//2, cols//2
    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i-crow)**2 + (j-ccol)**2)
            mask[i, j] = 1 - np.exp(-(d**2) / (2 * sigma**2))
    return mask

# Baca gambar
img = cv2.imread('k.jpg', 0)

# Lakukan transformasi Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Buat Butterworth Highpass Filter
rows, cols = img.shape
mask_butterworth = butterworth_hpfilter(rows, cols, 50, 2)

# Buat Gaussian Highpass Filter
mask_gaussian = gaussian_hpfilter(rows, cols, 50)

# Aplikasikan filter pada gambar dalam domain frekuensi
fshift_butterworth = fshift * mask_butterworth
fshift_gaussian = fshift * mask_gaussian

# Kembalikan gambar ke domain spasial
f_ishift_butterworth = np.fft.ifftshift(fshift_butterworth)
img_back_butterworth = np.fft.ifft2(f_ishift_butterworth)
img_back_butterworth = np.abs(img_back_butterworth)

f_ishift_gaussian = np.fft.ifftshift(fshift_gaussian)
img_back_gaussian = np.fft.ifft2(f_ishift_gaussian)
img_back_gaussian = np.abs(img_back_gaussian)

# Tampilkan gambar hasil
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img_back_butterworth, cmap = 'gray')
plt.title('Butterworth HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_back_gaussian, cmap = 'gray')
plt.title('Gaussian HPF'), plt.xticks([]), plt.yticks([])
plt.show()
