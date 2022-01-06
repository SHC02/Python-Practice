import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Dog', rescaleFrame(img))

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', rescaleFrame(blue))
cv.imshow('Green', rescaleFrame(green))
cv.imshow('Red', rescaleFrame(red))

cv.imshow('Blue', rescaleFrame(b))
cv.imshow('Green', rescaleFrame(g))
cv.imshow('Red', rescaleFrame(r))

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', rescaleFrame(merged))

cv.waitKey(0)