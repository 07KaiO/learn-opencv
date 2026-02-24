# Buổi 01: Cấu trúc Ma trận ảnh & Đọc/Ghi dữ liệu.

1. Bản chất của một bức ảnh trong OpenCVTrong OpenCV, một bức ảnh không phải là một file .jpg hay .png. Khi được nạp vào bộ nhớ, nó là một Ma trận đa chiều (Numpy Array).Ảnh Xám (Grayscale): Là ma trận 2 chiều ($Rows \times Cols$). Mỗi phần tử là một số từ 0 (Đen) đến 255 (Trắng).Ảnh Màu (Color): Là ma trận 3 chiều ($Rows \times Cols \times Channels$). OpenCV sử dụng hệ màu BGR (Blue, Green, Red). Mỗi điểm ảnh (pixel) sẽ là một danh sách gồm 3 giá trị màu.
   
---

2. Các hàm cơ bản nhất (Hello World của OpenCV)
Bạn hãy tạo một file `buoi1.py` và thử đoạn mã sau:
```
import cv2

# 1. Đọc ảnh (im-read)
# Tham số 1: Đường dẫn file. Tham số 2: 1 (màu), 0 (xám)
img = cv2.imread('path_to_your_image.jpg', 1)

# 2. Kiểm tra cấu trúc ma trận (Kích thước ảnh)
# Kết quả trả về: (Chiều cao, Chiều rộng, Số kênh màu)
print(f"Kích thước ảnh: {img.shape}")

# 3. Hiển thị ảnh (im-show)
cv2.imshow('Cua so hien thi', img)

# 4. Ghi ảnh ra file khác (im-write)
cv2.imwrite('anh_copy.png', img)

# 5. Giữ cửa sổ mở cho đến khi nhấn phím
cv2.waitKey(0) 
cv2.destroyAllWindows()
```

---

3. Tại sao lại là BGR mà không phải RGB?
Đây là một "di sản" lịch sử. Khi OpenCV mới ra đời, các nhà sản xuất camera và phần mềm thường ưu tiên định dạng BGR. OpenCV giữ nguyên điều này để tương thích.

Lưu ý: Khi bạn dùng các thư viện khác như Matplotlib để hiển thị ảnh từ OpenCV, ảnh sẽ bị "sai màu" (đỏ thành xanh) nếu bạn không chuyển đổi ngược lại.

---

4. Bài tập thực hành cho bạnĐể kết thúc buổi 1, bạn hãy thực hiện thử thách này:Đọc một tấm ảnh màu bất kỳ.In ra giá trị Pixel tại tọa độ $(x=100, y=100)$. (Gợi ý: print(img[100, 100])).Thử thách: Bạn hãy tìm cách đọc ảnh đó nhưng ở dạng Ảnh Xám (Grayscale) ngay từ hàm cv2.imread và hiển thị nó lên.