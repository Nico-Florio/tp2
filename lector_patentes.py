import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


#IMPRESION DE IMAGEN (BLANCO Y NEGRO)
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#QUITA TONALIDADES MEDIAS DE GRISES (UMBRAL)
def apply_threshold(img):
    return cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)[1]


#IMPRESION DE IMAGEN
def plot_image(img, grayscale=True):
    plt.axis('off')
    if grayscale:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


img = cv2.imread(r'imgs\024.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (800, 400))
#plot_image(img)


img = grayscale(img)
#plot_image(img)


img = apply_threshold(img)
#plot_image(img)


#img = cv2.Canny(img, 30, 200) ENFASIS EN BORDES
#plot_image(img)


contours=cv2.findContours(img.copy(),cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]
screenCnt = None

for c in contours:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    # if our approximated contour has four points, then
    # we can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break

mask = np.zeros(img.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(img,img,mask=mask)

plot_image(new_image)