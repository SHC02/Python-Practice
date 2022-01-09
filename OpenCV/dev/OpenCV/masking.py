import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Dog', rescaleFrame(img))

# blank image with the first two values
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', rescaleFrame(blank))

# Create rectangle mask
mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2),(img.shape[1]//2 + 100, img.shape[0]//2 + 100), \
    100, 255, -1)
cv.imshow('Mask', rescaleFrame(mask))

# Override image on the mask with bitwise AND
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', rescaleFrame(masked))

cv.waitKey(0)