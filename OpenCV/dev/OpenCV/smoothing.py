import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Dog', rescaleFrame(img))


cv.waitKey(0)