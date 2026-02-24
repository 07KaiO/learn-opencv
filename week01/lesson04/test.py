import cv2

img = cv2.imread('image/download.jpeg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('hsv_img', hsv_img)

print(hsv_img[100,200])
cv2.waitKey(0)
cv2.destroyAllWindows()