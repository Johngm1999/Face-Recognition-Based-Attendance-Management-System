# import re
import re
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
import csv
from tkinter import filedialog
import tkinter as tk

#Global variable for importCsv Function 
mydata=[]
class Issue:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x768+0+0")
        self.root.state('zoomed')
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend = tk.StringVar(value="")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\banner.jpg")
        img=img.resize((1600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=130)

        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg2.jpg")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Feedback Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=70,width=1520,height=550)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Issue Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=40,y=10,width=700,height=300)

        

        # ==================================Text boxes and Combo Boxes====================
        
        #Student id


        studentId_id = Label(left_frame,text="Issue Id:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_id.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        student_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        student_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

       

        studentId_label = Label(left_frame,text="Response:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=1  ,column=0,padx=5,pady=5,sticky=W)

      


        self.studentId_entry = tk.Text(left_frame, width=20, height=5, font=("verdana", 12, "bold"))
        self.studentId_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
  
        # ===============================Table Sql Data View==========================
     
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=0,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=150,width=635,height=60)

        #Improt button
        save_btn=Button(btn_frame,command=self.escalate_data,text="Send",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)


    

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Issue Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=780,y=10,width=660,height=500)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=70,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("Issue_ID","Student_ID","Name","Issue","Description","Response"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("Issue_ID",text="Issue_ID")
        self.attendanceReport.heading("Student_ID",text="Student_ID")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Issue",text="Issue")
        self.attendanceReport.heading("Description",text="Date")
        self.attendanceReport.heading("Response",text="Response")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("Issue_ID",width=100)
        self.attendanceReport.column("Student_ID",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Issue",width=100)
        self.attendanceReport.column("Description",width=100)
        self.attendanceReport.column("Response",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================

    # ===============================update function for mysql database=================
    import mysql.connector
    from tkinter import messagebox

    def escalate_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Response", "Do you want to Respond this Issue?", parent=self.root)
                if Update:
                    response_text = self.studentId_entry.get("1.0", END)  # Get the text from the Text widget
                    conn = mysql.connector.connect(user='root', password='', host='localhost', database='face_recognition', port=3306)
                    mycursor = conn.cursor()
                    
                    update_query = "UPDATE issue SET Response=%s WHERE Is_id=%s"
                    data = (response_text.strip(), self.var_id.get())  # Use response_text.strip() to remove leading/trailing whitespaces
                    mycursor.execute(update_query, data)

                    conn.commit()
                    mycursor.close()
                    conn.close()

                    messagebox.showinfo("Success", "Successfully Replied!", parent=self.root)
                    self.fetch_data()  # Assuming this function fetches and updates the data display
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # =============================Delete Attendance form my sql============================
    
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("SELECT * FROM issue")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):

        self.var_attend.set("")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        



    #=============Cursur Function for CSV========================



     #=============Cursur Function for mysql========================

    def get_cursor_right(self, event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0])
        self.var_dep.set(data[1])
        self.var_name.set(data[2])
        self.var_time.set(data[3])
        self.var_date.set(data[4])

        # Instead of setting self.var_attend to the widget, get its value
        attend_text = data[5] if data[5] else ""  # Check if data[5] is None, and set it to an empty string if it is
        self.var_attend.set(attend_text) 
    

if __name__ == "__main__":
    root=Tk()
    obj=Issue(root)
    root.mainloop()