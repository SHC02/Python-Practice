import cv2 as cv
import numpy as np

blankImage = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blankImage)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Dog', img)

# 1. paint the image a certain color
#blankImage[200:300, 300:400] = 0,255,0
#cv.imshow('Green', blankImage)

# 2. Draw a rectangle
cv.rectangle(blankImage, (0,0), (blankImage.shape[1]//2, blankImage.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blankImage)

# 3. Draw a circle
cv.circle(blankImage, (blankImage.shape[1]//2, blankImage.shape[0]//2), 40, (0,0,255), thickness = -1)
cv.imshow('Circle', blankImage)

# 4. Draw a line
cv.line(blankImage,(100,250), (300,400), (255,255,0), thickness=3)
cv.imshow('line', blankImage)

# 5. Write text on image
cv.putText(blankImage, 'Hello World?', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blankImage)

cv.waitKey(0)
