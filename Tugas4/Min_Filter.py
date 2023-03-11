import numpy as np
import cv2


def complex_min_filter(img, kernel_size):
    # Menambahkan gambar
    img = cv2.copyMakeBorder(img, kernel_size // 2, kernel_size // 2, kernel_size // 2, kernel_size // 2,
                             cv2.BORDER_CONSTANT)
    filtered_img = np.zeros_like(img)

    for i in range(kernel_size // 2, img.shape[0] - kernel_size // 2):
        for j in range(kernel_size // 2, img.shape[1] - kernel_size // 2):
            # Membagi gambar menjadi tiga channel warna
            b, g, r = cv2.split(
                img[i - kernel_size // 2:i + kernel_size // 2 + 1, j - kernel_size // 2:j + kernel_size // 2 + 1])
            # Menerapkan min filter pada channel saluran
            b_min = np.min(b)
            g_min = np.min(g)
            r_min = np.min(r)
            # Menggabungkan channel yang difilter menjadi satu gambar
            filtered_img[i, j] = [b_min, g_min, r_min]

    return filtered_img[kernel_size // 2:filtered_img.shape[0] - kernel_size // 2,
           kernel_size // 2:filtered_img.shape[1] - kernel_size // 2]


# Membaca gambar yang digunakan
img = cv2.imread('Mawar.png')

# Menerapkan filter median
filtered_img = complex_min_filter(img, 3)

# Menampilkan hasil
cv2.imshow('Original', img)
cv2.imshow('Complex Min Filter', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
