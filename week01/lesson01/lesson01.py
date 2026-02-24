import cv2

# Đọc ảnh màu Lenna
img_color = cv2.imread('image/download.jpeg')
# Đọc ảnh Coins nhưng ép về chế độ Xám (số 0)
img_gray = cv2.imread('image/download.png', 0)

print(f"Shape của ảnh màu: {img_color.shape}") 
# Kết quả sẽ có 3 con số (H, W, 3)

print(f"Shape của ảnh xám: {img_gray.shape}")
# Kết quả chỉ có 2 con số (H, W)

cv2.imshow('Mau', img_color)
cv2.imshow('Xam', img_gray)
cv2.waitKey(0)