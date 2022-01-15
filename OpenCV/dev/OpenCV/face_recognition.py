import numpy as np
import cv2 as cv

# reading xml file with classifier
haar_cascade = cv.CascadeClassifier('OpenCV/dev/OpenCV/haar_face.xml')

people = ['50 cent', 'Dr Dre', 'Eminem', 'Frank Ocean', 'Daniel Caesar']
# features = np.load('features.npy', allow_pickle= True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'C:\Users\takem\Desktop\Python-Practice\OpenCV\dev\OpenCV\face_trained.yml')

img = cv.imread(r'C:\Users\takem\Desktop\Python-Practice\OpenCV\dev\OpenCV\Photos\Training\Eminem\eminem1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('50 Cent', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[x:x+w, y:y+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {[confidence]}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, fontScale = 1.0, color = (0,255,0), thickness = 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    
cv.imshow('Detected FACE', img)

cv.waitKey(0)
