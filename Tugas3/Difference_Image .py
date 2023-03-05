import cv2

# memuat dua gambar
img_first = cv2.imread('gambar1.jpg')
img_second = cv2.imread('gambar2.jpg')

# ubah menjadi ukuran yang sama
img_first = cv2.resize(img_first, (400, 400))
img_second = cv2.resize(img_second, (400, 400))

# ubah gambar menjadi skala abu-abu
gray_img1 = cv2.cvtColor(img_first, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img_second, cv2.COLOR_BGR2GRAY)

# menghitung perbedaan absolut anatara kedua gambar
diff_img = cv2.absdiff(gray_img1, gray_img2)

# Threshold perbedaan gambar
thresh = cv2.threshold(diff_img, 25, 255, cv2.THRESH_BINARY)[1]

# menampilkan hasil
cv2.imshow('Gambar1', img_first)
cv2.imshow('Gambar2', img_second)
cv2.imshow('Difference Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
