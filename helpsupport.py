from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x768+0+0")
        self.root.state('zoomed')
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\banner.jpg")
        img=img.resize((1600,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1600,height=130)

        # backgorund image 
        bg1=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\bg4.png")
        bg1=bg1.resize((1600,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1600,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",25,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1600,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
       

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\cnt.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.contact,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=550,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.contact,text="Contact us",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=550,y=380,width=180,height=45)

        
         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\91628\Desktop\Face-Recognition-Attendance1\Images_GUI\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=800,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Mail us",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=800,y=380,width=180,height=45)


        # create function for button 
    
    
    def contact(self):
        self.new = 1
        self.url = "https://wa.me/<number>"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()