import numpy as np
import cv2
from matplotlib import pyplot as plt

def unsharp_masking(img, alpha, kernel_size):
    blur = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    mask = cv2.addWeighted(img, 1+alpha, blur, -alpha, 0)
    return mask

def laplacian_filter(rows, cols):
    laplacian_kernel = np.zeros((rows, cols), np.uint8)
    laplacian_kernel[int(rows/2), int(cols/2)] = 4
    laplacian_kernel[int(rows/2), int(cols/2)-1] = -1
    laplacian_kernel[int(rows/2), int(cols/2)+1] = -1
    laplacian_kernel[int(rows/2)-1, int(cols/2)] = -1
    laplacian_kernel[int(rows/2)+1, int(cols/2)] = -1
    return laplacian_kernel

def selective_filtering(img, threshold, mask_size):
    mask = cv2.medianBlur(img, mask_size)
    diff = cv2.absdiff(img, mask)
    return cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)[1]

# Baca gambar
img = cv2.imread('k.jpg', 0)

# Lakukan transformasi Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Buat Unsharp Masking
unsharp_mask = unsharp_masking(img, 1.5, 5)

# Buat Laplacian Domain Frekuensi
rows, cols = img.shape
laplacian_kernel = laplacian_filter(rows, cols)
fshift_laplacian = fshift * laplacian_kernel
img_back_laplacian = np.fft.ifft2(np.fft.ifftshift(fshift_laplacian))
img_back_laplacian = np.abs(img_back_laplacian)

# Buat Selective Filtering
selective_filtered = selective_filtering(img, 20, 7)

# Tampilkan gambar hasil
plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(unsharp_mask, cmap = 'gray')
plt.title('Unsharp Masking'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_back_laplacian, cmap = 'gray')
plt.title('Laplacian Domain Frekuensi'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(selective_filtered, cmap = 'gray')
plt.title('Selective Filtering'), plt.xticks([]), plt.yticks([])
plt.show()
