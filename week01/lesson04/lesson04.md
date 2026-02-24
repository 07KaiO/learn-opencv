# 🌈 Buổi 04: Không gian màu (Color Spaces)
Đây là bài học quan trọng nhất để chuẩn bị cho việc Nhận diện vật thể.

1. Tại sao cần nhiều không gian màu?
Mặc dù BGR rất tốt để hiển thị trên màn hình, nhưng nó cực kỳ tệ nếu bạn muốn tách một vật thể dựa trên màu sắc (ví dụ: tách quả cam ra khỏi đống táo). Tại sao? Vì trong BGR, khi ánh sáng thay đổi (bóng tối đổ xuống), cả 3 giá trị B, G, R đều thay đổi hỗn loạn.

2. Hệ màu HSV (Cực kỳ quan trọng)
Để giải quyết vấn đề ánh sáng, người ta dùng HSV:

H (Hue): Sắc thái màu (Đỏ, Vàng, Xanh...). Đây là thông số giúp ta chọn đúng màu cần tìm.

S (Saturation): Độ bão hòa (Màu đậm hay nhạt/xám).

V (Value): Độ sáng.

Ưu điểm: Khi ánh sáng thay đổi, chủ yếu giá trị V thay đổi, còn H (màu sắc thực) vẫn khá ổn định. Đây là lý do HSV được dùng 90% trong các bài toán lọc màu.

3. Cách chuyển đổi trong OpenCV
```
# Chuyển BGR sang Xám (Gray)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Chuyển BGR sang HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

---

Bạn hãy chuyển tấm ảnh màu của mình sang hệ HSV.

Thử truy cập vào một pixel hsv_img[y, x]. Bạn sẽ thấy 3 giá trị, nhưng hãy nhớ: con số đầu tiên (H) lúc này không phải là màu Xanh dương nữa, mà là Góc của màu sắc trên vòng tròn màu.

Câu hỏi: Bạn có biết tại sao trong OpenCV, giá trị H chỉ chạy từ 0 đến 179, trong khi vòng tròn màu thực tế là 360 độ không?