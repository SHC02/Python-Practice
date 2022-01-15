import os
import cv2 as cv
import numpy as np
#1-15-2022

people = ['50 cent', 'Dr Dre', 'Eminem', 'Frank Ocean', 'Daniel Caesar']
DIR = r'C:\Users\takem\Desktop\Python-Practice\OpenCV\dev\OpenCV\Photos\Training'

# reading xml file with classifier
haar_cascade = cv.CascadeClassifier('OpenCV/dev/OpenCV/haar_face.xml')

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for image in os.listdir(path):
            img_path = os.path.join(path, image)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Done')

features = np.array(features, dtype = 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features lists and the labels list
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)