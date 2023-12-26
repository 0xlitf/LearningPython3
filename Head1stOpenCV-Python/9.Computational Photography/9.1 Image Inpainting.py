import cv2 as cv
import matplotlib
import numpy as np
import sys
from matplotlib import pyplot as plt
import inspect
from PySide6.QtWidgets import QApplication, QWidget

matplotlib.use("QtAgg", force=True)
plt.ion()


def function():
    current_function_name = inspect.currentframe().f_code.co_name
    print("current_function_name:", current_function_name)

    img = cv.imread('../data/messi_2.jpg')
    mask = cv.imread('../data/mask2.png', 0)
    dst = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    function()

    sys.exit(app.exec())
