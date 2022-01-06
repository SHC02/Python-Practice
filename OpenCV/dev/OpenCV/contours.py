import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Dog', rescaleFrame(img))

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', rescaleFrame(blank))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', rescaleFrame(gray))

#canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny Edges', rescaleFrame(canny))

#blur = cv.GaussianBlur(canny, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blurred', rescaleFrame(blur))

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshed', rescaleFrame(thresh))

# By using blurred image to this method, the countours reduced.
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found!')


# Draw all the contours on the blank image
# drawContours = using blank image, adding contours, -1 means adding all up , colors, thickness
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', rescaleFrame(blank))

cv.waitKey(0)