import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import faces
import mysql.connector

window = tk.Tk()
window.title("FRAS-Face Recognition Attendance System")

window.geometry('1280x720')
window.configure(background='white')
Notification = tk.Label(window, text="All things good", bg="Green", fg="white", width=15,
                        height=3, font=('times', 17))

import tkinter as tk
def del_sc1():
    sc1.destroy()
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry('300x100')
    # sc1.iconbitmap('AMS.ico')
    sc1.title('Warning!!')
    sc1.configure(background='grey80')
    Label(sc1, text='Student_ID & Name required!!!', fg='black',
          bg='white', font=('times', 16)).pack()
    Button(sc1, text='OK', command=del_sc1, fg="black", bg="lawn green", width=9,
           height=1, activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)


def take_img():
    def testVal(inStr, acttyp):
        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False
        return True

    wind = tk.Tk()
    wind.geometry("1400x800")
    wind.configure(background='Grey')
    wind.title("Student Registration")
  
    lbl = tk.Label(wind, text="Student_ID : ", width=20, height=2,
                fg="black", bg="grey", font=('times', 15, 'bold'))
    lbl.place(x=300, y=10)

    txt = tk.Entry(wind, validate="key", width=20, bg="white",
                    fg="black", font=('times', 25))
    txt['validatecommand'] = (txt.register(testVal), '%P', '%d')
    txt.place(x=550, y=10)

    lbl2 = tk.Label(wind, text="Name : ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl2.place(x=300, y=90)

    txt2 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt2.place(x=550, y=90)

    lbl3 = tk.Label(wind, text="Department : ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl3.place(x=300, y=190)

    txt3 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt3.place(x=550, y=190)

    lbl4 = tk.Label(wind, text="C. Code: ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl4.place(x=300, y=290)

    txt4 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt4.place(x=550, y=290)

    lbl5 = tk.Label(wind, text="Section : ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl5.place(x=300, y=390)

    txt5 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt5.place(x=550, y=390)
    
    lbl6 = tk.Label(wind, text="Schedule Day : ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl6.place(x=300, y=490)

    txt6 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt6.place(x=550, y=490)
    
    lbl7 = tk.Label(wind, text="Schedule Time : ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl7.place(x=300, y=590)

    txt7 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt7.place(x=550, y=590)
    
    lbl8 = tk.Label(wind, text="Room Number : ", width=20, fg="black",
                    bg="grey", height=2, font=('times', 15, ' bold '))
    lbl8.place(x=300, y=690)

    txt8 = tk.Entry(wind, width=20, bg="white",
                    fg="black", font=('times', 25))
    txt8.place(x=550, y=690)
    
    def insert():
        Student_ID = int(txt.get())
        name = txt2.get()
        department = txt3.get()
        cc = txt4.get()
        section = txt5.get()
        sche_day = txt6.get()
        sche_time = txt7.get()
        room_no = txt8.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO student (ID, Name, Department, C_Code, Section, Schedule_Day, Schedule_Time, Room_Number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (Student_ID, name, department, cc, section, sche_day, sche_time, room_no)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    
    def scan_face_and_save():
        l1 = txt.get()
        l2 = txt2.get()
        if l1 == '':
            err_screen()
        elif l2 == '':
            err_screen()
        else:
            try:
                # Start video capture
                cam = cv2.VideoCapture(0)
                detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                    # Get the data from the labels
                Student_ID = txt.get()
                Name = txt2.get()
                Department= txt3.get()
                C_Code = txt4.get()
                Section = txt5.get()
                Schedule_Day = txt6.get()
                Time = txt7.get()
                Room = txt8.get()
                sampleNum = 0
                while (True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                            # incrementing sample number
                        sampleNum = sampleNum + 1
                        
                    # Check if all data is provided
                        if not all([Department, C_Code, Section, Schedule_Day, Time, Room]):
                            lbl_all_data = tk.Label(wind, text="All data is required", width=20, height=2,
                                                    fg="red", bg="white", font=('times', 15, 'bold'))
                            lbl_all_data.place(x=1000, y=400)
                        else:
                            cv2.imwrite("Training Image/ " + Student_ID + "." + Name + '.' + str(sampleNum) + ".jpg",
                                                gray)
                            print("Images Saved")
                            cv2.imshow('Frame', img)
                        
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                        # Release the video capture
                    elif sampleNum > 30:
                        break
                    cam.release()
                    cv2.destroyAllWindows()
                    
                ts = time.time()
                Schedule_Day = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                row = [Student_ID, Name, Department, C_Code, Section, Schedule_Day, Time, Room]
                with open('C:/FaceR/Student Details/StudentDetails1.csv', 'a+') as csvFile:
                    writer = csv.writer(csvFile, delimiter=',')
                    writer.writerow(row)
                    csvFile.close()
                res = "Images Saved : " + Student_ID + " Name : " + Name
                Notification.configure(
                    text=res, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
                Notification.place(x=270, y=250)
            except FileExistsError as f:
                    f = 'Student Data already exists'
                    Notification.configure(text=f, bg="Red", width=21)
                    Notification.place(x=270, y=250)
                    
                    
                    
    takeImg = tk.Button(wind, text="Submit", command=scan_face_and_save, fg="black", bg="SkyBlue1",
                        width=20, height=1, activebackground="white", font=('times', 15, ' bold '))
    takeImg.place(x=1000, y=550)
    wind.mainloop()
                
takeImg = tk.Button(window, text="Registration", command=take_img, fg="black", bg="Grey",
                    width=20, height=3, activebackground="white", font=('times', 15, ' bold '))
takeImg.place(x=200, y=350)  



def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces, Id
        faces, Id = getImagesAndLabels('Training Image')
    except Exception as e:
        l = 'please make "Training Image" folder & put Images'
        Notification.configure(text=l, bg="SpringGreen3",
                               width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)
    
    recognizer.train(faces, np.array(Id)) 
    try:
        recognizer.save("Training Image Label/Trainner.yml")
        
    except Exception as e:
        q = 'Please make "TrainingImageLabel" folder'
        Notification.configure(text=q, bg="SpringGreen3",
                                width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    res = "Model Trained"  # +",".join(str(f) for f in Id)
    Notification.configure(text=res, bg="olive drab",
                        width=50, font=('times', 18, 'bold'))
    Notification.place(x=270, y=250)
    


def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = detector.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as Id of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

trainImg = tk.Button(window, text="Train Images", fg="black", command=trainimg, bg="Grey",
                     width=20, height=3, activebackground="white", font=('times', 15, ' bold '))
trainImg.place(x=500, y=350)

import subprocess

def run_script():
    subprocess.call(["python", "C:/FRAS/test2.py"])

run_script_button = tk.Button(window, text="User Log", command=run_script, bg="Grey", 
                            height=3, width=20, activebackground="white", font=('times', 15, ' bold '))
run_script_button.place(x=800, y=350)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def admin():
    subprocess.call(["python", "C:/FRAS/admin.py"])
AP = tk.Button(window, text="Check Registered Students", command=admin, fg="black",
               bg="SkyBlue1", width=20, height=2, activebackground="white", font=('times', 15, ' bold '))
AP.place(x=500, y=500)

def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", on_closing)

message = tk.Label(window, text="Face Recognition Registration", bg="SkyBlue", fg="black", width=47,
                   height=3, font=('times', 30, ' bold '))

message.place(x=80, y=20)

window.mainloop()  