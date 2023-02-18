import cv2
import numpy as np
import datetime
import time
import os
import csv

# Load the pre-trained face detection model
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the face recognition model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.read("Training Image Label/Trainner.yml")

# Define the ID-Name mapping
id_name_map = {11310: "Sim", 10715: "Hitape", 10867: "Magno"}

with open("student_details.csv", "w") as file:
    file.write("ID,Name,Confidence,Date,Time In,Time Out\n")
    
    # Start capturing video from the default camera
    cap = cv2.VideoCapture(0)
    
    while True:
        # Capture a video frame
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Loop through the faces
        for (x, y, w, h) in faces:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Get the face region of interest
            roi_gray = gray[y:y+h, x:x+w]

            # Predict the ID and confidence of the face
            id, confidence = face_recognizer.predict(roi_gray)

            # Get the name of the person
            Name = id_name_map.get(id," ")
             
            current_datetime = datetime.datetime.now()
            time_in = current_datetime.time()
            time_out = None
        
            # Print the ID, name, and confidence on the frame
            cv2.putText(frame, f"ID: {id}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.putText(frame, f"Name: {Name}", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.putText(frame, f"Percent: {confidence}", (x, y-70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
  
            # Write the ID, name, and confidence to the CSV file
            with open("student_details.csv", "w") as file:
                file.write(f"{id},{Name},{confidence},{current_datetime.date()},{time_in},{time_out}\n")
            
            #time.sleep(60)
        # Display the frame
        cv2.imshow("Automated Face Recognition Attendance System", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Close the file
        file.close()

    # Release the video capture
    cap.release()

    # Destroy all windows
    cv2.destroyAllWindows()
