# Lab 05: Xử lý luồng Video từ Webcam.
Thực chất, video chỉ là một chuỗi các tấm ảnh (frames) được hiển thị liên tiếp với tốc độ rất nhanh. Nếu bạn xử lý được một tấm ảnh, bạn sẽ xử lý được video.

---

1. Cấu trúc cơ bản để mở Webcam
Để làm việc với Video, chúng ta sử dụng đối tượng `cv2.VideoCapture`.

```
import cv2

# 0 là ID của webcam mặc định. Nếu bạn có 2 camera, thử số 1.
cap = cv2.VideoCapture(0)

while True:
    # Đọc từng khung hình (frame) từ webcam
    # ret: biến boolean (True nếu đọc thành công)
    # frame: chính là ma trận ảnh (giống như khi dùng cv2.imread)
    ret, frame = cap.read()

    if not ret:
        break

    # Hiển thị frame lên cửa sổ
    cv2.imshow('Webcam Live', frame)

    # Nhấn phím 'q' trên bàn phím để thoát vòng lặp
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
```

---

2. Giải thích các "điểm lạ" trong code Video
2.1 `cv2.waitKey(1)`:

Ở ảnh tĩnh, ta dùng 0 để dừng vô tận.

Ở video, ta dùng 1 (1 mili giây). Nó có 2 tác vụ: Đợi phím nhấn và tạo một khoảng nghỉ cực ngắn để màn hình kịp hiển thị frame tiếp theo. Nếu không có dòng này, webcam của bạn sẽ bị "treo".

2.2 `cap.release()`: Cực kỳ quan trọng! Nó ra lệnh cho hệ điều hành: "Tôi dùng xong camera rồi, hãy tắt đèn LED và cho phép ứng dụng khác sử dụng nó".

---

3. Bài tập Lab 05: "Hệ thống giám sát Mini"
Bây giờ, hãy vận dụng kiến thức từ Buổi 2, 3 và 4 để biến Webcam bình thường thành một công cụ phân tích. Bạn hãy viết một đoạn code thực hiện các yêu cầu sau:

3.1 Mở Webcam.

3.2 Vẽ một khung chữ nhật cố định ở chính giữa màn hình (giả sử đây là vùng cần giám sát).

3.3 Viết chữ "LIVE" màu đỏ nhấp nháy hoặc cố định ở góc trên màn hình.

3.4 Cắt (Crop) vùng ảnh bên trong hình chữ nhật đó và hiển thị nó ra một cửa sổ riêng có tên là "Vung_Giam_Sat".

3.5 Chuyển cửa sổ "Vung_Giam_Sat" sang màu xám (Grayscale).

