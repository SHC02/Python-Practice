import cv2 as cv
import matplotlib.pyplot as plt

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')
cv.imshow('Dog', rescaleFrame(img))

#plt.imshow(img)
#plt.show()

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', rescaleFrame(gray))

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', rescaleFrame(hsv))

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB', rescaleFrame(lab))

# BGR to RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rescaleFrame(RGB))

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -> BGR', rescaleFrame(hsv_bgr))

plt.imshow(RGB)
plt.show()

cv.waitKey(0)