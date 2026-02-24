# Buổi 02: Hệ tọa độ & Các hàm vẽ cơ bản.

1. Hệ tọa độ trong OpenCV (Nhắc lại và Đào sâu)
Khác với hệ tọa độ Oxy trong toán học (gốc O ở dưới bên trái), trong xử lý ảnh:

- Gốc tọa độ (0, 0): Nằm ở góc Trên cùng bên Trái.

- Trục X (Width): Chạy từ trái sang phải.

- Trục Y (Height): Chạy từ trên xuống dưới.
  
2. Các hàm vẽ cơ bản
Một điểm cực kỳ thú vị: Các hàm vẽ của OpenCV sẽ thay đổi trực tiếp trên biến ảnh mà bạn truyền vào.

a. Vẽ đường thẳng (Line)
```
# cv2.line(anh, diem_dau, diem_cuoi, mau_sac, do_day)
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 5)
```
- `(255, 0, 0)`: Màu Blue (vì là hệ BGR).

- `5`: Độ dày nét vẽ (pixel).

b. Vẽ hình chữ nhật (Rectangle) - Rất hay dùng để làm Bounding Box
```
# cv2.rectangle(anh, goc_tren_trai, goc_duoi_phai, mau_sac, do_day)
cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 3)
```
Nếu bạn để độ dày là -1, nó sẽ tô đặc hình chữ nhật đó.

c. Vẽ hình tròn (Circle)
```
# cv2.circle(anh, tam, ban_kinh, mau_sac, do_day)
cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)
```

d. Viết chữ (Text)
```
# cv2.putText(anh, "Noi dung", toa_do, font, ti_le, mau, do_day)
cv2.putText(img, "OpenCV Mentor", (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
```