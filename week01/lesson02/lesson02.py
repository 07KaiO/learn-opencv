import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype="uint8")

cv2.line(canvas, (0, 0), (511, 511), 255, 5)

cv2.rectangle(canvas, (100, 100), (300, 300), 255, 3)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)