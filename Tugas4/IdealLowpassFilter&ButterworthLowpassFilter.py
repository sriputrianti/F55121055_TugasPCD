import numpy as np
import cv2
from matplotlib import pyplot as plt

def ideal_lpfilter(rows, cols, radius):
    mask = np.zeros((rows, cols), np.uint8)
    crow, ccol = rows//2, cols//2
    for i in range(rows):
        for j in range(cols):
            if np.sqrt((i-crow)**2 + (j-ccol)**2) <= radius:
                mask[i, j] = 1
    return mask

def butterworth_lpfilter(rows, cols, radius, n):
    mask = np.zeros((rows, cols), np.uint8)
    crow, ccol = rows//2, cols//2
    for i in range(rows):
        for j in range(cols):
            d = np.sqrt((i-crow)**2 + (j-ccol)**2)
            mask[i, j] = 1 / (1 + (d/radius)**(2*n))
    return mask

# Baca gambar
img = cv2.imread('k.jpg', 0)

# Lakukan transformasi Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Buat Ideal Lowpass Filter
rows, cols = img.shape
mask_ideal = ideal_lpfilter(rows, cols, 50)

# Buat Butterworth Lowpass Filter
mask_butterworth = butterworth_lpfilter(rows, cols, 50, 2)

# Aplikasikan filter pada gambar dalam domain frekuensi
fshift_ideal = fshift * mask_ideal
fshift_butterworth = fshift * mask_butterworth

# Kembalikan gambar ke domain spasial
f_ishift_ideal = np.fft.ifftshift(fshift_ideal)
img_back_ideal = np.fft.ifft2(f_ishift_ideal)
img_back_ideal = np.abs(img_back_ideal)

f_ishift_butterworth = np.fft.ifftshift(fshift_butterworth)
img_back_butterworth = np.fft.ifft2(f_ishift_butterworth)
img_back_butterworth = np.abs(img_back_butterworth)

# Tampilkan gambar hasil
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(img_back_ideal, cmap = 'gray')
plt.title('Ideal LPF'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_back_butterworth, cmap = 'gray')
plt.title('Butterworth LPF'), plt.xticks([]), plt.yticks([])
plt.show()
