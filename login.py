from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
from train import Train
from student import Student
from train import Train
from Issue import Issue
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.state('zoomed')
        self.root.geometry("1600x768+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\log1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)
        self.password_var = tk.StringVar()
        #entry2 
        self.txtpwd = ttk.Entry(frame1, font=("times new roman", 15, "bold"), show="*", textvariable=self.password_var)
        
        self.txtpwd.place(x=33,y=260,width=270)

        self.show_pwd_button = ttk.Button(frame1, text="Show", command=self.toggle_password_visibility)

        self.show_pwd_button .place(x=33,y=290,width=60,height=20)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.on_login_button_click,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Mark Attendance",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=150,height=20)


        
    def toggle_password_visibility(self):
        # Toggle the show/hide option for the password entry                
        current_show_option = self.txtpwd.cget("show")
        new_show_option = "" if current_show_option == "*" else "*"
        self.txtpwd.config(show=new_show_option)

    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def on_login_button_click(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Admin","Welcome to Attendance Managment System Using Facial Recognition")
            Face_Recognition_System(root)
            
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from student where Email=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                messagebox.showinfo("Sussessfully","Welcome to User Portal")
                User_Portal(root,self.txtuser.get())
    
        
        




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x768+0+0") #1366
        self.root.state('zoomed')
       # self.root.attributes('-fullscreen', True)
        self.root.title("Face_Recogonition_System")
     

    
# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg1.jpg")
        img=img.resize((1600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg1.jpg")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text=" Face Recognition Based Smart Attendance System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=100,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="User Registration",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=100,y=380,width=180,height=45)

        
         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=350,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Track Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=350,y=380,width=180,height=45)

        #  # Help  Support  button 4
        # hlp_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\hlp.jpg")
        # hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        # self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        # hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2",)
        # hlp_b1.place(x=400,y=400,width=180,height=180)

        #hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Help and Support",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="navyblue")
        #hlp_b1_1.place(x=1300,y=600,width=160,height=40)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=600,y=200,width=180,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Image Training",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        tra_b1_1.place(x=600,y=380,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\gmail.png")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.issue,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=850,y=200,width=180,height=180)

        pho_b1_1 = Button(bg_img,command=self.issue,text="Issues",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        pho_b1_1.place(x=850,y=380,width=180,height=45)

        # # Developers   button 7
        
        #dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("tahoma",12,"bold"),bg="white",fg="navyblue")
        #dev_b1_1.place(x=1300,y=550,width=160,height=40)


        

        # # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.close_login_and_open_main,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=1100,y=200,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.close_login_and_open_main,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=1100,y=380,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
         os.startfile("dataset")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def issue(self):
        self.new_window=Toplevel(self.root)
        self.app=Issue(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)
    
    def Close(self):
        self.root.destroy()
        new_window = tk.Toplevel()  # Create a new Toplevel window
        app = Login(new_window) 
    def close_login_and_open_main(self):
        # Destroy the login page widgets
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "login.py"])
        
        
    
    




#student portal
class User_Portal:
    def __init__(self,root,email):
        self.root=root
        self.root.geometry("1600x768+0+0") #1366
        self.root.state('zoomed')
       # self.root.attributes('-fullscreen', True)
        self.root.title("Face_Recogonition_System")
        self.email=email

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg1.jpg")
        img=img.resize((1600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg1.jpg")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text=" Student Portal",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=50)


          # student button 1
        std_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.profile,image=self.std_img1,cursor="hand2")
        std_b1.place(x=200,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.profile,text="Student Profile",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=200,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.attendancelist,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=450,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.attendancelist,text="Track Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=450,y=380,width=180,height=45)


        issue_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\tra.jpg")
        issue_img_btn=issue_img_btn.resize((180,180),Image.ANTIALIAS)
        self.issue_img1=ImageTk.PhotoImage(issue_img_btn)

        issue_b1 = Button(bg_img,command=self.issue1,image=self.issue_img1,cursor="hand2",)
        issue_b1.place(x=700,y=200,width=180,height=180)

        issue_b1_1 = Button(bg_img,command=self.issue1,text="Issue Reporting",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        issue_b1_1.place(x=700,y=380,width=180,height=45)

         

        
        # # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.close_login_and_open_main,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=950,y=200,width=180,height=180)

        exi_b1_1 = Button(bg_img,command=self.close_login_and_open_main,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        exi_b1_1.place(x=950,y=380,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
         os.startfile("dataset")
# ==
    def profile(self):
        self.new_window=Toplevel(self.root)
        self.app=profile(self.new_window,self.email)

    def attendancelist(self):
        self.new_window=Toplevel(self.root)
        self.app=att(self.new_window,self.email)

    def issue1(self):
        self.new_window=Toplevel(self.root)
        self.app=Issue1(self.new_window,self.email)
    
    def Close(self):
        self.root.destroy()  # Destroy the current window
        login_window = tk.Tk()
        Login(login_window)
    def close_login_and_open_main(self):
        # Destroy the login page widgets
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "login.py"])



import tkinter as tk
from tkinter import messagebox
import mysql.connector

class profile:
    def __init__(self, root, email):
        self.root = root
        self.root.geometry("1600x768+0+0")  # Set window size
        self.root.title("Student Profile")
        
        self.email = email

        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg1.jpg")
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
        title_lb1 = Label(bg_img,text=" Student Portal",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=50)

        
        # Create labels to display student details
        self.lbl_name = tk.Label(root, text="Name:", font=("Arial", 26), bg="white", fg="black")
        self.lbl_name.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.lbl_email = tk.Label(root, text="Email:", font=("Arial", 26), bg="white", fg="black")
        self.lbl_email.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.lbl_department = tk.Label(root, text="Department:", font=("Arial", 26), bg="white", fg="black")
        self.lbl_department.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        # Fetch student details from the database
        self.fetch_student_details()
        # Add the Update button
        #update_btn = Button(root, text="Update", font=("Arial", 18), command=self.open_update_page)
        #update_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def fetch_student_details(self):
        try:
            # Establish database connection
            connection = mysql.connector.connect(
                username='root', password='', host='localhost',
                database='face_recognition', port=3306
            )
            
            cursor = connection.cursor()
            
            # Execute the query to retrieve student details
            query = "SELECT Name, Email, Department FROM student WHERE Email = %s"
            cursor.execute(query, (self.email,))
            
            # Fetch the first row
            row = cursor.fetchone()
            
            # Check if a student with the given email exists
            if row is not None:
                # Display student details
                self.lbl_name.config(text="Name: " + row[0])
                self.lbl_email.config(text="Email: " + row[1])
                self.lbl_department.config(text="Department: " + row[2])
            else:
                # Show error message if student not found
                messagebox.showerror("Error", "Student not found!")
            
        except mysql.connector.Error as error:
            # Show error message if there's a database error
            messagebox.showerror("Database Error", str(error))
        
        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    def open_update_page(self):
        # Create a new window for updating student details
        update_window = Toplevel(self.root)
        update_page = UpdatePage(update_window, email=self.email, profile_window=self.root)


    def open_img(self):
         os.startfile("dataset")
    def open_update_page(self):
        # Create a new window for updating student details
        update_window = Toplevel(self.root)
        update_page = UpdatePage(update_window, email=self.email,profile_window=self.root)




class att:
    def __init__(self, root, email):
        self.root = root
        self.root.geometry("1600x768+0+0")  # Set window size
        self.root.title("Student Profile")
        
        self.email = email

        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg1.jpg")
        img=img.resize((1600,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=100)

        # backgorund image 
        bg1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=100,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Student Portal",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=50)

        
        # Right section=======================================================
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=70,width=1520,height=550)
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=5,y=70,width=1520,height=550)


        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=40,width=1500,height=300)

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


        # Set Width of Colums \
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

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        cursor = conn.cursor()
        query="select StudentID from student where Email= %s"
        cursor.execute(query, (self.email,))    
        row = cursor.fetchone()
        self.row=row
        print(row)
        mycursor = conn.cursor()
        query1="select * from stdattendance where std_id= %s"
        mycursor.execute(query1, row) 
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()





class UpdatePage:
    def __init__(self, root, email,profile_window):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Update Student Details")
        self.profile_window = profile_window
        self.email = email

        # Create labels and entry fields for updating student details
        self.lbl_name = Label(root, text="Name:", font=("Arial", 18))
        self.lbl_name.pack(pady=10)

        self.entry_name = Entry(root, font=("Arial", 18))
        self.entry_name.pack(pady=10)

        self.lbl_email = Label(root, text="Email:", font=("Arial", 18))
        self.lbl_email.pack(pady=10)

        self.entry_email = Entry(root, font=("Arial", 18))
        self.entry_email.pack(pady=10)

        self.lbl_department = Label(root, text="Department:", font=("Arial", 18))
        self.lbl_department.pack(pady=10)

        self.entry_department = Entry(root, font=("Arial", 18))
        self.entry_department.pack(pady=10)

        # Fetch and display the current student details
        self.fetch_student_details()

        # Add the Update button
        update_btn = Button(root, text="Update", font=("Arial", 18), command=self.update_student_details)
        update_btn.pack(pady=20)

    def fetch_student_details(self):
        try:
            # Establish database connection
            connection = mysql.connector.connect(
                username='root', password='', host='localhost',
                database='face_recognition', port=3306
            )

            cursor = connection.cursor()

            # Execute the query to retrieve student details
            query = "SELECT Name, Email, Department FROM student WHERE Email = %s"
            cursor.execute(query, (self.email,))

            # Fetch the first row
            row = cursor.fetchone()

            # Check if a student with the given email exists
            if row is not None:
                # Display student details in the entry fields
                self.entry_name.insert(0, row[0])
                self.entry_email.insert(0, row[1])
                self.entry_department.insert(0, row[2])
            else:
                # Show error message if student not found
                messagebox.showerror("Error", "Student not found!")

        except mysql.connector.Error as error:
            # Show error message if there's a database error
            messagebox.showerror("Database Error", str(error))

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def update_student_details(self):
        # Get the updated student details from the entry fields
        name = self.entry_name.get()
        email = self.entry_email.get()
        department = self.entry_department.get()
        try:
            # Establish database connection
            connection = mysql.connector.connect(
                username='root', password='', host='localhost',
                database='face_recognition', port=3306
            )

            cursor = connection.cursor()

            # Execute the query to update student details
            query = "UPDATE student SET Name = %s, Email = %s, Department = %s WHERE Email = %s"
            cursor.execute(query, (name, email, department, self.email))
            connection.commit()
            
            # Show success message
            messagebox.showinfo("Success", "Student details updated successfully!")
            self.root.destroy()
            self.profile_window.destroy()
            Login(root)
        except mysql.connector.Error as error:
            # Show error message if there's a database error
            messagebox.showerror("Database Error", str(error))

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()





class Issue1:
    
    def __init__(self,root,email):
        self.root=root
        self.root.geometry("1600x768+0+0")
        self.root.state('zoomed')
        self.root.title("Attendance Pannel")
        self.email1=email

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_dep=StringVar()
        self.var_name=StringVar()
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

          #time
        time_label = Label(left_frame,text="Issue",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Description",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)


        

        # ===============================Table Sql Data View==========================
     
    

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=0,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=150,width=635,height=60)

        #Improt button
        save_btn=Button(btn_frame,command=self.add_data,text="Submit",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
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
        self.attendanceReport.heading("Description",text="Description")
        self.attendanceReport.heading("Response",text="Response")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("Issue_ID",width=100)
        self.attendanceReport.column("Student_ID",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Issue",width=100)
        self.attendanceReport.column("Description",widt=200)
        self.attendanceReport.column("Response",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # =================================update for mysql button================

    # ===============================update function for mysql database=================
 
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        cursor = conn.cursor()
        query="select StudentID,Name from student where Email= %s"
        cursor.execute(query, (self.email1,))    
        row = cursor.fetchone()
        self.id=row[0]
        self.name=row[1]
        print(self.id,self.name)
        mycursor = conn.cursor()
        query1="select * from issue where Student_ID= %s"
        mycursor.execute(query1,(self.id,)) 
        data=mycursor.fetchall()            

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_dep.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def add_data(self):
        if self.var_time.get()=="" or self.var_date.get=="" :           
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()
                query="select StudentID,Name from student where Email= %s"
                cursor.execute(query, (self.email1,))    
                row = cursor.fetchone()
                self.id=row[0]
                self.name=row[1]
                mycursor = conn.cursor()
            
                mycursor.execute("insert into issue(Student_ID,Name,Issue,Description,Response) values(%s,%s,%s,%s,'')",(
                (self.id),
                (self.name),
                self.var_time.get(),
                self.var_date.get(),

               
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

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

        self.var_id.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])    
   




if __name__ == "__main__":
        root = tk.Tk()
        app = Login(root)
        root.mainloop()
        

    


