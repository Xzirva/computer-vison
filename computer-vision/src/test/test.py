import cv2 as cv
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.ion()
img = cv.imread("/projects/computer-vision/opencv-course/Resources/Photos/cat.jpg")
plt.imshow(img)