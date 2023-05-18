import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

model = AccidentDetectionModel("model.json", 'model_weights.h5')
font = cv2.FONT_HERSHEY_SIMPLEX
my_w = tk.Tk()
my_w.geometry("410x300")
my_w.title('Accident Detection')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Upload the Video',width=30,font=my_font1)  
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda:open_file())
b1.grid(row=2,column=1,columnspan=4)
def open_file():
    filepath = tk.filedialog.askopenfilename()
    if filepath is not None:
        startapplication(filepath)

def startapplication(filepath):
    vid=open(filepath,'r')
    video = cv2.VideoCapture(vid.name)
    vid.close()
    
    
    while True:
        ret, frame = video.read()
        if not ret:
            return prob
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
        if(pred == "Accident"):
            prob = (round(prob[0][0]*100, 2))

            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            cv2.putText(frame, pred+" "+str(prob), (20, 30), font, 1, (255, 255, 0), 2)

        if cv2.waitKey(33) & 0xFF == ord('q'):
            return 
        cv2.imshow('Video', frame) 
         
if __name__ == '__main__':
    open_file()


