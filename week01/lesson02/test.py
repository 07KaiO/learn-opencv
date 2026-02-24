import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype="uint8")

cv2.rectangle(canvas, (100, 100), (156+256, 156+256), (0, 0, 255), -1)

cv2.circle(canvas, (256, 256), 30, (0, 255, 255), -1)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)