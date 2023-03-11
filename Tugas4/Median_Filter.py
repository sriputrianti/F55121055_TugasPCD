import numpy as np
import cv2


def complex_median_filter(img, kernel_size):
    # Menambahkan gambar
    img = cv2.copyMakeBorder(img, kernel_size // 2, kernel_size // 2, kernel_size // 2, kernel_size // 2,
                             cv2.BORDER_CONSTANT)
    filtered_img = np.zeros_like(img)

    for i in range(kernel_size // 2, img.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, img.shape[1] - kernel_size // 2):
            # Membagi gambar menjadi tiga channel warna
            b, g, r = cv2.split(
                img[i - kernel_size // 2:i + kernel_size // 2 + 1, j - kernel_size // 2:j + kernel_size // 2 + 1])
            # Menerapkan median filter pada channel saluran
            b_median = np.median(b)
            g_median = np.median(g)
            r_median = np.median(r)
            # Menggabungkan channel yang difilter menjadi satu gambar
            filtered_img[i, j] = [b_median, g_median, r_median]

    return filtered_img[kernel_size // 2:filtered_img.shape[0] - kernel_size // 2,
           kernel_size // 2:filtered_img.shape[1] - kernel_size // 2]


# Membaca gambar yang digunakan
img = cv2.imread('Mawar.png')

# Menerapkan filter median
filtered_img = complex_median_filter(img, 3)

# Menampilkan hasil
cv2.imshow('Original', img)
cv2.imshow('Complex Median Filter', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

