import cv2

#membaca gambar
img_first=cv2.imread("Mawar.png")

#ubah ukuran gambar
img_first = cv2.resize(img_first, (450, 450))

#menggunakan ukuran 5x5
img_blur = cv2.blur(img_first,(5,5))


#menampilkan gambar buram
window_name="image_blur"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.imshow ("Mawar.png",img_first)
cv2.imshow ("image_blur",img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

