from tkinter import *
from PIL import Image,ImageTk
import cv2

root=Tk()
faces_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")

cap=cv2.VideoCapture(1)
Lframe=LabelFrame(root,text="bruce",font=("times new roman",30,"bold"),bg="black",fg="gray")
Lframe.pack()
my_label=Label(Lframe,bg="green")
my_label.pack()

while True:
    success,img=cap.read()
    faces=faces_cascade.detectMultiScale(img,1.5,5)
    smiles=smile_cascade.detectMultiScale(img)
    for x,y,w,z in faces[:]:
        cv2.rectangle(img,(x,y),(x+w,y+z),(0,225,0),2) 
    #for q,t,e,r in smiles[:]:
    #    cv2.rectangle(img,(q,t),(q+e,t+r),(0,0,255))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=ImageTk.PhotoImage(Image.fromarray(img))
    my_label['image']=img
    root.update()




