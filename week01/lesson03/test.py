import cv2

img = cv2.imread('image/download.jpeg')

width = int(img.shape[1] * 0.5)
height = int(img.shape[0] * 0.5)

cv2.imshow("Original", img)
cv2.imshow("200x200", img[height-100:height+100, width-100:width+100])

cv2.waitKey(0)