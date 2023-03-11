import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca gambar dan konversi ke b grayscale
img = cv2.imread('kopi.jpg', 0)

# Lakukan DFT pada gambar
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Buat filter frekuensi dalam domain frekuensi
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)
mask = np.zeros((rows, cols, 2), np.uint8)
r = 60
mask[crow-r:crow+r, ccol-r:ccol+r] = 1

# Aplikasikan filter pada gambar
dft_shift_filtered = dft_shift * mask

# Kembalikan gambar ke domain spasial
dft_filtered = np.fft.ifftshift(dft_shift_filtered)
img_back = cv2.idft(dft_filtered, flags=cv2.DFT_SCALE | cv2.DFT_COMPLEX_OUTPUT)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Tampilkan gambar hasil
plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap='gray')
plt.title('Gambar Hasil'), plt.xticks([]), plt.yticks([])
plt.show()
