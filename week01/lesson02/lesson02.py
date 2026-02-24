import cv2
import numpy as np

# Tạo ảnh đen kích thước 512x512, 3 kênh màu
# np.zeros tạo ma trận toàn số 0. uint8 là kiểu dữ liệu (0-255)
canvas = np.zeros((512, 512, 3), dtype="uint8")

# Vẽ một hình chữ nhật màu xanh lá
cv2.rectangle(canvas, (100, 100), (400, 400), (0, 255, 0), 3)

# Vẽ một hình tròn đỏ ở giữa
cv2.circle(canvas, (256, 256), 50, (0, 0, 255), -1)

# Ghi chữ lên ảnh
cv2.putText(canvas, "BUOI 02 DONE!", (150, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Drawing", canvas)
cv2.waitKey(0)