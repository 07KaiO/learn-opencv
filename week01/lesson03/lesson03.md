# Buổi 03: Phép biến đổi hình học (Geometric Transformations).
Hôm nay chúng ta sẽ học cách "nhào nặn" bức ảnh. Trong thực tế, không phải lúc nào tấm ảnh bạn thu được cũng hoàn hảo. Đôi khi bạn cần phóng to để nhìn rõ hơn, cắt bỏ phần thừa, hoặc xoay ảnh cho đúng chiều.

Trong OpenCV, 3 phép biến đổi quan trọng nhất là: Resize (Thay đổi kích thước), Crop (Cắt ảnh) và Rotate (Xoay ảnh).

1. Thay đổi kích thước (Resize)
   Hàm này dùng để phóng to hoặc thu nhỏ ảnh.

```
# cv2.resize(anh, (chieu_rong, chieu_cao))
img_resized = cv2.resize(img, (300, 200))
```
- Lưu ý: Thứ tự ở đây là (Width, Height), ngược lại với shape của ma trận.

- Ứng dụng: Làm nhỏ ảnh lại để các thuật toán AI xử lý nhanh hơn.

2. Cắt ảnh (Crop) - Sức mạnh của Numpy Slicing
Đây là điều thú vị nhất: OpenCV không có hàm cv2.crop.
Vì ảnh là một ma trận (Numpy array), chúng ta dùng kỹ thuật "cắt mảng" (Slicing) để lấy một phần của ảnh.
```
# img[y_dau : y_cuoi, x_dau : x_cuoi]
img_cropped = img[0:200, 200:500]
```

3. Xoay ảnh (Rotation)
Xoay ảnh trong OpenCV phức tạp hơn một chút vì bạn phải xác định một "Ma trận xoay".
```
# 1. Xác định tâm xoay, góc xoay (ví dụ 45 độ) và tỉ lệ thu phóng (1.0 là giữ nguyên)
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# 2. Thực hiện xoay
img_rotated = cv2.warpAffine(img, matrix, (w, h))
```

4. Tổng hợp thực hành Buổi 3

```
import cv2

img = cv2.imread('lena.jpg')

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
```