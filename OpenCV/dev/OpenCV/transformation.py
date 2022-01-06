import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('OpenCV/dev/OpenCV/Photos/dog1.jpg')

cv.imshow('Dog', rescaleFrame(img))

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down

# translate image 100 pixels moving right, 100 pixels down
translated = translate(img, 100, 100)
cv.imshow('Translated', rescaleFrame(translated))    
    

# Rotation
def rotating(img, angle, rotation_point = None):
    (height, width) = img.shape[:2]
    if rotation_point is None:
        rotation_point = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

# Counterclockwise rotating 45 degree
# if you want to change to clockwise, change to negative value
rotated_image = rotating(img, 45)
cv.imshow('Rotated', rescaleFrame(rotated_image))

rotated_rotated = rotating(rotated_image, -45)
cv.imshow('Rotated_rotated', rescaleFrame(rotated_rotated))

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flip
# flipcode can be -1 = vertical flip, 1 = horizontal flip, 0 = vertical flip
fliped = cv.flip(img, 0)
cv.imshow('Fliped', rescaleFrame(fliped))

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
