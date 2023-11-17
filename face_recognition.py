# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x768+0+0")
        self.root.state('zoomed')
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\banner.jpg")
        img=img.resize((1600,140),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=140)

        # backgorund image 
        bg1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg2.jpg")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=60)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\f_det.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=650,y=180,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=650,y=360,width=180,height=45)
    #=====================Attendance===================

    from datetime import datetime
    import csv
    def mark_attendance(self, id, r, n):
        import csv
        name_list = []
        name_list1=[]
        with open("a.csv", "r+") as f:
            reader=f.readlines()
            for entry in reader:
                if len(entry) >= 5:
                   entry=entry.split((","))
                   name_list.append(entry[4])
                   name_list1.append(entry[0])
                    
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M")
            
            if id not in name_list1:
                writer = csv.writer(f,lineterminator='\n')
                writer.writerow([id, r, n, dtString, d1, "Present"])
        # Example usage:
        input_file_path = "a.csv"
        output_file_path = "attendance.csv"
        self.remove_duplicates_from_csv(input_file_path, output_file_path)
                 
            
       
                       

                    

    def remove_duplicates_from_csv(self,input_file, output_file):
        import csv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        unique_first_column_values = set()
        unique_rows = []

        # Read the CSV file and store unique rows in the list
        with open(input_file, "r", newline="") as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Skip the header row if present
            for row in reader:
                first_column_value = row[0]
                if first_column_value not in unique_first_column_values:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    unique_first_column_values.add(first_column_value)
                    unique_rows.append(row)

        # Write the unique rows back to the CSV file
        with open(output_file, "w", newline="") as outfile:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
            writer = csv.writer(outfile)
   
            writer.writerows(unique_rows)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       


    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()

                
                   
                my_cursor.execute("select Department from student where StudentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                
                my_cursor.execute("select Name from student where StudentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                print(confidence)

                if confidence > 80:
                    cv2.putText(img,f"Student_ID:{id}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Department:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(id,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 27:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()