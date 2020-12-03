import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
import sklearn
import pickle
import cv2

haar = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
# pickle files
model_svm  = pickle.load(open('./model/model_svm_pca100.pickle','rb'))
model_pca  = pickle.load(open('./model/pca_100.pickle','rb'))

print('Model loaded sucessfully')

# settins
gender_pre = ['Male','Female']
font = cv2.FONT_HERSHEY_SIMPLEX


def pipeline_model(path,filename,color='bgr'):
    # step-1: read image in cv2
    img = cv2.imread(path)
    # step-2: convert into gray scale
    if color == 'bgr':
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # step-3: crop the face (using haar cascase classifier)
    faces = haar.detectMultiScale(gray,1.5,3)
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) # drawing rectangle
        cropped_img = gray[y:y+h,x:x+w] # crop image
        # step - 4: normalization (0-1)
        cropped_img = cropped_img / 255.0
        # step-5: resize images (100,100)
        if cropped_img.shape[1] > 100:
            cropped_img_resize = cv2.resize(cropped_img,(100,100),cv2.INTER_AREA)
        else:
            cropped_img_resize = cv2.resize(cropped_img,(100,100),cv2.INTER_CUBIC)
        # step-6: Flattening (1x10000)
        cropped_img_reshape = cropped_img_resize.reshape(1,10000) # 1,-1
        # step -7: get eigen image
        eigen_image = model_pca.transform(cropped_img_reshape)
        # step -8: pass to ml model (svm)
        results = model_svm.predict_proba(eigen_image)[0]
        # step -9:
        predict = results.argmax() # 0 or 1 
        score = results[predict]
        # step -10:
        text = "%s : %0.2f"%(gender_pre[predict],score)
        cv2.putText(img,text,(x,y),font,1,(0,255,0),3)
    
    cv2.imwrite('./static/predict/{}'.format(filename),img)
    