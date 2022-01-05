import cv2 as cv

img = cv.imread('Photos/dog1.jpg')

cv.imshow('Dog', img)

# Resize image
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
 

# keyboard binding function
# wait for a specific delay and key to be pressed
cv.waitKey(0)

