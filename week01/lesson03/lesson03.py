import cv2

img = cv2.imread('image/download.png')

# 1. Resize ảnh về một nửa kích thước ban đầu
width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)
img_half = cv2.resize(img, (width, height))

# 2. Crop lấy khuôn mặt (Tọa độ này ước lượng cho ảnh Lena chuẩn)
face = img[200:400, 200:400]

# 3. Xoay ngược ảnh 180 độ (Cách nhanh nhất không dùng ma trận)
img_flip = cv2.flip(img, -1) 

cv2.imshow("Original", img)
cv2.imshow("Half Size", img_half)
cv2.imshow("Face Only", face)
cv2.imshow("Flipped", img_flip)

cv2.waitKey(0)