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

#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x768+0+0")
        self.root.state('zoomed')
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_attid=StringVar()
        self.var_id=StringVar()
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

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
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=70,width=1520,height=550)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=40,y=10,width=700,height=500)

        

        # ==================================Text boxes and Combo Boxes====================
        studentattId_label = Label(left_frame,text="Att-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentattId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentattId_entry = ttk.Entry(left_frame,textvariable=self.var_attid,width=15,font=("verdana",12,"bold"))
        studentattId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        #Student id
        studentId_label = Label(left_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Student Roll
        student_roll_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Department
        # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        # ===============================Table Sql Data View==========================
        


    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(main_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=50,y=200,width=635,height=60)



        #Exprot button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Clear CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Upload",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)

        refresh_btn=Button(btn_frame,command=self.refresh_data,text="Refresh",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        refresh_btn.grid(row=0,column=4,padx=6,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=780,y=10,width=660,height=500)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("Att_Id","ID","Department","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)


        self.attendanceReport.heading("Att_Id",text="Att_Id")
        self.attendanceReport.heading("ID",text="Std-ID")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("Att_Id",width=100)
        self.attendanceReport.column("ID",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================
    #Update button
        del_btn=Button(right_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #Update button
        del_btn=Button(right_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
    # ===============================update function for mysql database=================
    def update_data(self):
        if self.var_id.get()=="" or self.var_dep.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_department=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_att_id =%s",( 
                    
                    self.var_id.get(),
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_attid.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_attid.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where std_att_id=%s"
                    val=(self.var_attid.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select std_att_id, std_id, std_department, std_name, std_time, std_date, std_attendance from stdattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_attid.set(""),
        self.var_id.set("")
        self.var_dep.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    def refresh_data(self):
    # Step 1: Clear existing data
        self.attendanceReport.delete(*self.attendanceReport.get_children())

        # Step 2: Fetch updated data (assuming self.fetch_data() does this)
        updated_data = self.fetch_data()  # Replace this with your data-fetching logic

        # Step 3: Populate the Treeview with the new data
        for record in updated_data:
            self.attendanceReport.insert("", "end", values=record)

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)                                                                                                                                                                                                                                                                                      
            

    #==================Experot CSV=============
    def exportCsv(self):
        
        file_path = "attendance.csv"
        if file_path:
            with open(file_path, "w", newline=""):
                pass                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            file_path1= "a.csv"
            if file_path1:
                with open(file_path1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                , "w", newline=""):
                    pass
           
                    messagebox.showinfo("Successfuly","CSV Cleared Successfully!",parent=self.root)
                   

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]
        
        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_attid.set(data[0])
        self.var_id.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_name.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attend.set(data[6])     
    #=========================================Update CSV============================

        # export upadte
    import csv
    import mysql.connector

    def action(self):
        try:
            conn = mysql.connector.connect(
                username='root',
                password='',
                host='localhost',
                database='face_recognition',
                port=3306
            )
            mycursor = conn.cursor()

            with open("attendance.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                 # Skip the header row if present

                for row in reader:
                    print(row)
                    std_id, std_department, std_name, std_time, std_date, std_attendance = row

                    mycursor.execute("INSERT INTO stdattendance (std_id, std_department, std_name, std_time, std_date, std_attendance) VALUES (%s, %s, %s, %s, %s, %s)", (
                        std_id,
                        std_department,
                        std_name,
                        std_time,
                        std_date,
                        std_attendance
                    ))

                    conn.commit()  # Commit inside the loop for each row

            self.fetch_data()  # Fetch data after all rows are inserted
            conn.close()
            messagebox.showinfo("Success", "All Records are Saved in the Database!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



    #     conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognition',port=3307)
    #     mycursor = conn.cursor()
    #     if messagebox.askyesno("Confirmation","Are you sure you want to save attendance on database?"):
    #         for i in mydata:
    #             uid = i[0]
    #             uroll = i[1]
    #             uname = i[2]
    #             utime = i[3]
    #             udate = i[4]
    #             uattend = i[5]
    #             qury = "INSERT INTO stdattendance(std_id, std_roll_no, std_name, std_time, std_date, std_attendance) VALUES(%s,%s,%s,%s,%s,%s)"
    #             mycursor.execute(qury,(uid,uroll,uname,utime,udate,uattend))
    #         conn.commit()
    #         conn.close()
    #         messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
    #     else:
    #         return False




        # 









if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()