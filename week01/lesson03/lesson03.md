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

---

1. Giả sử bạn có một tấm ảnh kích thước 600 x 800 (Cao 600, Rộng 800).Bạn muốn Cắt (Crop) lấy một hình vuông ở chính giữa ảnh, có kích thước 200 x 200. Bạn sẽ viết dòng lệnh img[y1:y2, x1:x2] như thế nào?
2. Câu hỏi tư duy: Nếu bạn Resize một tấm ảnh nhỏ xíu lên một kích thước cực lớn, tấm ảnh sẽ bị hiện tượng gì?

Hiện tượng đó trong chuyên môn gọi là nhiễu pixel (pixelation) hoặc mất chi tiết (blurring).

🔍 Tại sao lại bị như vậy?
Hãy tưởng tượng tấm ảnh nhỏ của bạn là một bức tranh ghép hình (puzzle) có 100 mảnh. Khi bạn phóng nó lớn lên gấp 10 lần, máy tính buộc phải tạo ra 10.000 mảnh từ 100 mảnh ban đầu.

Vì máy tính không biết những chi tiết "mới" ở giữa các pixel cũ trông như thế nào, nó phải thực hiện một thuật toán gọi là Nội suy (Interpolation) - hiểu nôm na là "đoán" màu sắc cho các pixel mới dựa trên các pixel xung quanh.