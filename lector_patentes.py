import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def plot_image(img, grayscale=True):
    plt.axis('off')
    if grayscale:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


img = cv2.imread(r'imgs\000.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (600,300) )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plot_image(img)
