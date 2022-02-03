from email import message
import email
from typing import final
from django.http import HttpResponse
from pydoc import ModuleScanner
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import CameraIntegration
from CameraIntegration.models import DataSet, bodypartdb,contact
import cv2
import threading
import mediapipe as mp
import sys
import time
import pandas as pd
import numpy as np
import os
import pandas as pd
#import csv
#import seaborn as sns
import numpy as np
#import networkx as nx
#import graphviz
#from IPython.display import display
from collections import defaultdict
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MultiLabelBinarizer, StandardScaler
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree 
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpHands = mp.solutions.hands
hands = mpHands.Hands()
finallist=[]
organ_dict = {
        0: "Nose/ नाक",
        1: "Left Eye Inner/ आंख",
        2: "Left Eye/ आंख",
        3: "Left Eye Outer/ आंख",
        4: "Right Eye Inner/ आंख",
        5: "Right Eye/ आंख",
        6: "Right Eye Outer/ आंख",
        7: "Left Ear/ कान",
        8: "Right Ear/ कान",
        9: "Mouth Left/ मुंह",
        10: "Mouth Right/ मुंह",
        11: "Left Shoulder/ कंधा",
        12: "Right Shoulder/ कंधा",
        13: "Left Elbow/ कोहनी",
        14: "Right Elbow/ कोहनी",
        15: "Left Wrist/ कलाई",
        16: "Right Wrist/ कलाई",
        17: "Left Pinky/ कनिष्ठा",
        18: "Right Pinky/ कनिष्ठा",
        19: "Left Index/ अनुक्रमणिका",
        20: "Right Index/ अनुक्रमणिका",
        21: "Left Thumb/ अंगूठे",
        22: "Right Thumb/ अंगूठे",
        23: "Left Hip/ कूल्हा",
        24: "Right Hip/ कूल्हा",
        25: "Left Knee/ घुटना",
        26: "Right Knee/ घुटना",
        27: "Left Ankle/ टखने",
        28: "Right Ankle/ टखने",
        29: "Left Heel/ एड़ी",
        30: "Right Heel/ एड़ी",
        31: "Left Foot Index/ अनुक्रमणिका(टांग)",
        32: "Right Foot Index/ अनुक्रमणिका(टांग)"
}
dict_for_predict = {
        0: "nose",
        1: "eye",
        2: "eye",
        3: "eye",
        4: "eye",
        5: "eye",
        6: "eye",
        7: "ear",
        8: "ear",
        9: "mouth",
        10: "mouth",
        11: "shoulder",
        12: "shoulder",
        13: "elbow",
        14: "elbow",
        15: "wrist",
        16: "wrist",
        17: "fingers",
        18: "fingers",
        19: "fingers",
        20: "fingers",
        21: "fingers",
        22: "fingers",
        23: "hip",
        24: "hip",
        25: "knee",
        26: "knee",
        27: "ankle",
        28: "ankle",
        29: "heel",
        30: "heel",
        31: "foot",
        32: "foot"
}
arr_final = [[0]*2]*33
xAxisFinger,yAxisFinger=0,0
hFrame,wFrame=0,0
val_to_predict = None
# Create your views here.
class VideoCamera(object):
    t=0
    def __init__(self):
        self.t=time.time()
        self.video = cv2.VideoCapture(0)
        test = bodypartdb.objects.get(pk=1)
        test.part=None
        test.save()
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        #if(time.time()-self.t > 10):
            #print("Entered")
            #return NameError
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        global val_to_predict
        while True:
            cv2.putText(self.frame,str(int(time.time()-self.t)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            xAxisFinger=0
            yAxisFinger=0
            (self.grabbed, self.frame) = self.video.read()
            imgRGB = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)
            results = pose.process(imgRGB)
            if results.pose_landmarks:
                mpDraw.draw_landmarks(self.frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
                for id,lm in enumerate (results.pose_landmarks.landmark):
                    h,w,c = self.frame.shape
                    cx,cy=lm.x*w,lm.y*h
                    arr_final[id]=cx,cy
            results = hands.process(imgRGB)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        hFrame, wFrame, c = self.frame.shape
                        cx, cy = int(lm.x * wFrame), int(lm.y * hFrame)
                        cv2.circle(self.frame, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
                    mpDraw.draw_landmarks(self.frame, handLms, mpHands.HAND_CONNECTIONS)
                    x = (int)(handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].x * wFrame)
                    y = (int)(handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y * hFrame)
                    xAxisFinger=x
                    yAxisFinger=y
                    cv2.rectangle(self.frame, (x - 30, y - 30), (x + 30, y + 30), (255, 0, 255), 5)
            for ind,i in enumerate(arr_final):
                if((ind>=11 and ind<=14) or (ind>22 and ind<27)):
                    if abs(i[0]-xAxisFinger)<50 and abs(i[1]-yAxisFinger)<50:
                        cv2.rectangle(self.frame, (x - 100, y - 100), (x + 100, y + 100), (255, 00, 255), 5)
                        #print(organ_dict[ind])
                        #cv2.putText(self.frame,str(organ_dict[ind]),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
                        crop_img = self.frame[y-100:y + 100, x - 100:x + 100]
                        if((time.time()-self.t)>10):  
                            #a=testDB(name="Rishabh Vashist",part="Headache")
                            #a.save()
                            cv2.putText(self.frame,str("Close this tab now"),(100,300),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),5)    
                            cv2.putText(self.frame,str(organ_dict[ind]),(100,100),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),5)    
                            test = bodypartdb.objects.get(pk=1)
                            test.part=organ_dict[ind]
                            val_to_predict = dict_for_predict[ind]
                            test.save()
                            self.video.release()
                            #sys.exit(0)
            
                        #cv2.imshow("cropped", crop_img)
                        
                else:
                    if abs(i[0]-xAxisFinger)<10 and abs(i[1]-yAxisFinger)<10:
                        cv2.rectangle(self.frame, (x - 50, y - 50), (x + 50, y + 50), (255, 00, 255), 5)
                        #print(organ_dict[ind])
                        #cv2.putText(self.frame,str(organ_dict[ind]),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
                        crop_img = self.frame[y-50:y + 50, x - 50:x + 50]
                        if((time.time()-self.t)>10):  
                            #a=testDB(name="Rishabh Vashist",part="Headache")
                            #a.save()
                            cv2.putText(self.frame,str("Close this tab now"),(100,300),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),5)    
                            cv2.putText(self.frame,str(organ_dict[ind]),(100,100),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),5)    
                            test = bodypartdb.objects.get(pk=1)
                            test.part=organ_dict[ind]
                            val_to_predict = dict_for_predict[ind]
                            test.save()
                            self.video.release()
                            #sys.exit(0)
            
                        #cv2.imshow("cropped", crop_img)

def gen(cam):
    while True:
        frame = cam.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@gzip.gzip_page
def livefe(request):
    try:
        cam = VideoCamera()
        print("Welcome to dlt class")
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass


def page1(request):
    bodypart = bodypartdb.objects.all()
    set = bodypartdb.objects.values('part')
    print(set)
    dic={'Name':bodypart,'Part':set}
    return render(request,'Camera.html',dic)

def page2(request):
    test = bodypartdb.objects.get(pk=1)
    test.part=""
    test.save()             
    bodypart = bodypartdb.objects.all()
    set = bodypartdb.objects.values('part')
    dic={'Name':bodypart,'Part':set}
    return render(request,'Camera1.html',dic)


def symptom(request):
    path = os.path.join(os.path.dirname(__file__), 'files\hackathon.csv')
    df = pd.read_csv(path)
    print(val_to_predict)
    result = df.loc[df['body part'] == val_to_predict]
    result=result.replace(0,np.nan).dropna(axis=1,how="all")
    i=0
    list=[]
    print(result.columns)
    for col in result.columns.unique():
        if(i<3):
            i+=1
        else:
            list.append(col)
            i+=1
    dic = {  list[i]:i  for i in range(0, len(list) ) }
    dictionary ={'Part':dic,'Key':'yes'}
    result = request.POST
    print(result)
    res=result
    list=[]
    str=""
    for i in result:
        if(res[i]=='yes'):
            list.append(i)
            str=str+i+", "
            dictionary["Key"]="no"
    global finallist 
    finallist= list
        #***********************************************
    f = open("demofile2.txt", "w")
    f.writelines(str)
    f.close()
    return render(request,'Symptom.html',dictionary)

def predict(request):
    path = os.path.join(os.path.dirname(__file__), 'files\\hackathon.csv')
    dataset = pd.read_csv(path)
    dataset = dataset.drop(['body part', 'medical practitioner'] , axis='columns')
    y = dataset['diseases'].values
    X = dataset.drop('diseases', axis=1).values
    decision_tree = DecisionTreeClassifier()
    decision_tree = decision_tree.fit(X, y)
    y_pred = decision_tree.predict(X)
    dataset.drop('diseases', inplace=True, axis=1)
    ques=finallist
    inp=np.array([0]*453)
    list_of_column_names = list(dataset.columns)
    for i,val in enumerate(list_of_column_names):
        for j,val1 in enumerate(ques):
            if(val==val1):
                inp[i]=1
    arr=inp.reshape(1,-1)
    print(ques)
    pred_new = decision_tree.predict(arr)
    print(pred_new)
    Dictionary={'Name':pred_new[0]}
    return render(request,'Disease.html',Dictionary)

def department(request):
    path = os.path.join(os.path.dirname(__file__), 'files\\hackathon.csv')
    dataset = pd.read_csv(path)
    dataset = dataset.drop(['body part', 'medical practitioner'] , axis='columns')
    y = dataset['diseases'].values
    X = dataset.drop('diseases', axis=1).values
    decision_tree = DecisionTreeClassifier()
    decision_tree = decision_tree.fit(X, y)
    X = dataset.drop('diseases', axis = 1).values
    y_pred = decision_tree.predict(X)
    dataset.drop('diseases', inplace=True, axis=1)
    ques=finallist
    inp=np.array([0]*453)
    list_of_column_names = list(dataset.columns)
    for i,val in enumerate(list_of_column_names):
        for j,val1 in enumerate(ques):
            if(val==val1):
                inp[i]=1
    arr=inp.reshape(1,-1)
    pred_new = decision_tree.predict(arr)
    dl = pd.read_csv(path)
    u=dl['diseases']
    med=-1
    for i,val in enumerate (u):
        if(val==pred_new):
            med=i
    v=dl['medical practitioner']
    Dictionary={'Disease':pred_new[0],'Specialist':v[med]}
    return render(request,'Department.html',Dictionary)

def home(request):
    dict={"Key":"yes"}
    naam=None
    mail=None
    sub=None
    mes=None
    result=request.POST
    print(request)
    res=request.POST
    for i in result:
        dict["Key"]="no"
        if i=='name':
            naam=res[i]
        if i=='email':
            mail=res[i]
        if i=='subject':
            sub=res[i]
        if i=='message':
            mes=res[i]
    if(naam is not None and mail is not None):
        print(naam,mail,sub,mes)
        obj = contact.objects.create()
        obj.name=naam
        obj.email=mail
        obj.subject=sub
        obj.message=mes
        obj.save()
    return render(request,'index.html',dict)

def hindi(request):
    return render(request,'index_hindi.html')