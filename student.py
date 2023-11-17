from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
# Testing Connection 
"""
conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.state('zoomed')
        self.root.title("Student Pannel")

        #-----------Variables-------------------
        
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_dep=StringVar()
    
        
        

    # This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\banner.jpg")
        img=img.resize((1600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=130)

         # backgorund image 
        bg1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)




#title section
        title_lb1 = Label(bg_img,text="USER REGISTRAION",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=45)

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=70,width=1520,height=550)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="User Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=40,y=10,width=700,height=500)

        

        

       

        #Class Student Information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=10,y=20,width=635,height=230)

        #student id
        student_id_label = Label(class_Student_frame,text="Std-Id:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_id_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        student_id_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student name
        student_name_label = Label(class_Student_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #Email
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)


        #Password
        student_password_label = Label(class_Student_frame,text="Password:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_password_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        student_password_entry = ttk.Entry(class_Student_frame,textvariable=self.var_pass,width=15,font=("verdana",12,"bold"))
        student_password_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    


    

        dep_label=Label(class_Student_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=2,column=2,padx=5,pady=15)

        dep_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","MCA","MTECH","BTECH")
        dep_combo.current(0)
        dep_combo.grid(row=2,column=3,padx=5,pady=15,sticky=W)

        





       

       

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)







        #----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=780,y=10,width=660,height=500)

        #Searching System in Right Label Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=10,y=5,width=635,height=80)

        #Phone Number
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        #combo box 
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo["values"]=("Select","Student ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=120,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.student_table = ttk.Treeview(table_frame,column=("ID","Name","Email","Pass","Dep"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Pass",text="Password")
        self.student_table.heading("Dep",text="Department")
        
        self.student_table["show"]="headings"


        # Set Width of Colums 
        self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Pass",width=100)
        self.student_table.column("Dep",width=100)
        

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
# ==================Function Decleration==============================
    import re

    def add_data(self):
        import re
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_email.get() == "" or self.var_pass.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            # Check if the entered email is in a valid format
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
                messagebox.showerror("Error", "Invalid Email Format!", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(username='root', password='', host='localhost', database='face_recognition', port=3306)
                    mycursor = conn.cursor()

                    mycursor.execute("insert into student(StudentID,Name,Email,Password,Department) values(%s,%s,%s,%s,%s)", (
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_dep.get()
                    ))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "All Records are Saved!", parent=self.root)
                except Exception as es:
                    if "1062 (23000): Duplicate entry" in str(es):
                        messagebox.showerror("Error","Already Registerd Email or Student Id", parent=self.root)
                    else:
                        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================get cursor function=======================

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        print(data)
        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_email.set(data[2]),
        self.var_pass.set(data[3]),
        self.var_dep.set(data[4])
        
    # ========================================Update Function==========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get=="" or self.var_email.get()=="" or self.var_pass.get()=="":            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,Email=%s,Password=%s, Department=%s where StudentID =%s ",( 
                   
                    self.var_std_name.get(),
                self.var_email.get(),
                self.var_pass.get(),
                self.var_dep.get(),
                self.var_std_id.get()
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
    
    #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),)
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

    # Reset Function 


    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_email.set(""),
        self.var_pass.set(""),
        self.var_dep.set("Select Department")
        
    
    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT StudentID,Name,Email,Password,Department FROM student where StudentId='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                else:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#=====================This part is related to Opencv Camera part=======================
# ==================================Generate Data set take image=========================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get=="" or self.var_email.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                print(myreslut)
                id=0
                id1 = self.var_std_id.get()
                for x in myreslut:
                    id+=1

                    mycursor.execute("update student set Name=%s,Email=%s,Password=%s, Department=%s where StudentID=%s",( 
                    self.var_std_name.get(),
                self.var_email.get(),
                self.var_pass.get(),
                self.var_dep.get(),
                self.var_std_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/student."+str(id1)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main class object

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
