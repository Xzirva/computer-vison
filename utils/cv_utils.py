import cv2 as cv
import matplotlib.pyplot as plt

def cv_imshow(img, title):
    img_bgr = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img_bgr)

    if title is not None:
        plt.title(title)

    plt.show()