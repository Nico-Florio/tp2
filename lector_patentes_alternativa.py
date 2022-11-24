import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
import skimage
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


min_w=80 
max_w=110 
min_h=25 
max_h=52
ratio=3.07692307692


#IMPRESION DE IMAGEN (BLANCO Y NEGRO)
def grayscale(img): #listooo
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#QUITA TONALIDADES MEDIAS DE GRISES (UMBRAL)
def apply_threshold(img): #listooooo
    return cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)[1]


def apply_adaptive_threshold( img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 13)


def find_contours( img):
    return cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]


def filter_candidates(contours):
    candidates = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h
        if (np.isclose(aspect_ratio, ratio, atol=0.7) and
           (max_w > w > min_w) and
           (max_h > h > min_h)):
            candidates.append(cnt)
    return candidates



def get_lowest_candidate( candidates): #FUNCION IMPO
    ys = []
    for cnt in candidates:
        x, y, w, h = cv2.boundingRect(cnt)
        ys.append(y)
    return candidates[np.argmax(ys)]



def crop_license_plate( img, license):
    x, y, w, h = cv2.boundingRect(license)
    return img[y:y+h,x:x+w]


def clear_border( img):
    return skimage.segmentation.clear_border(img)


def invert_image( img):
    return cv2.bitwise_not(img)


def read_license( img, psm=7):
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    options += " --psm {}".format(psm)
    gray = grayscale(img)
    thresh = apply_threshold(gray)
    contours = find_contours(thresh)
    candidates = filter_candidates(contours)
    if candidates:
        license = candidates[0]
        if len(candidates) > 1:
            license = get_lowest_candidate(candidates)
        cropped = crop_license_plate(gray, license)
        thresh_cropped = apply_adaptive_threshold(cropped)
        clear_border = clear_border(thresh_cropped)
        final = invert_image(clear_border)
        txt = pytesseract.image_to_string(final, config=options)
        return txt
    else:
        return "No license plate found"

#IMPRESION DE IMAGEN
def plot_image(img, grayscale=True):
    plt.axis('off')
    if grayscale:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


img = cv2.imread(r'imgs\020.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (1362, 720))

#plot_image(img, False)

gray = grayscale(img)
plot_image(gray)
