import cv2 as cv

def rescaleFrame(frame, scale=0.25):
    # work for images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Original Image', rescaleFrame(img))

# Converting image color to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', rescaleFrame(gray))

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred', rescaleFrame(blur))

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', rescaleFrame(canny))

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', rescaleFrame(dilated))

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', rescaleFrame(eroded))

cv.waitKey(0)
