import cv2 as cv

img = cv.imread('OpenCV/dev/Photos/dog1.jpg')
cv.imshow('Dog', img)

def rescaleFrame(frame, scale=0.50):
    # work for images, videos, and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
    # only works for live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('OpenCV/dev/Videos/dog_video1.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()