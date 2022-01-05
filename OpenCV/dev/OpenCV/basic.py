import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    # work for images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/dog1.jpg')
cv.imshow('Dog', rescaleFrame(img))

# Converting image color to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', rescaleFrame(gray))

cv.waitKey(0)
