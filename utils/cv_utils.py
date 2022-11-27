import cv2 as cv
import matplotlib.pyplot as plt

def cv_imshow(title, img):
    img_bgr = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img_bgr)

    if title is not None:
        plt.title(title)

    plt.show()

def resize(src, scale=0.3):

    """
    Change the resolution of an existing video
    """
    #calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale)
    height = int(src.shape[0] * scale)

    return cv.resize(src, (width, height), interpolation=cv.INTER_AREA)

def change_res(capture, width, height):

    """
    Change resolution of a live input
    """

    capture.set(3, width)
    capture.set(4, height)
    return capture