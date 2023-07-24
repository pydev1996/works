from cgitb import text
#from curses.textpad import Textbox
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import PIL.Image
import tkinter.filedialog as fd
from resume_screening import *
from tkinter import ttk
from view_resume import *
# root = Tk()
# root.title('Automated Resume Screning')
# root.resizable(True, True)
# root.geometry('1500x750')
# root.configure(bg='ghost white')
#root.wm_attributes('-transparentcolor', '#ab23ff')
def main_page(root):
    titleframe = Frame(root,width="1500",height="750",bg="ghost white")
    titleframe.place(x=0,y=0)
    
    image=PIL.Image.open("4.jpg")
    
    img=image.resize((1400, 700))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( titleframe, image = my_img)
    label1.image = my_img
    label1.place(x = 0, y = 100)
    
    
    image=PIL.Image.open("image2.png")
    
    img=image.resize((100, 80))
    my_img=ImageTk.PhotoImage(img)
                # Show image using label
    label1 = Label( titleframe, image = my_img,bg='ghost white')
    label1.image = my_img
    label1.place(x = 70, y = 10)
    
    f= ("Farrah", 25, "bold")
    label1 = Label( titleframe, text="Automated Resume Screening",font=f,bg="ghost white",fg="red")
    label1.place(x = 320, y = 10)
    
    f= ("Times", 15, "bold")
    label1 = Label( titleframe, text="By Using NLP",font=f,bg="ghost white")
    label1.place(x = 340, y =50)
    def resume_screen():
        Name=StringVar()
        lgn_frame1 = Frame(titleframe, bg='#fc9714', width=1390, height=600,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=1, y=100)
        
        image4=PIL.Image.open("bg1.png")
        img4=image4.resize((1400, 700))
        my_img=ImageTk.PhotoImage(img4)
        
        label1 = Label(lgn_frame1, image = my_img)
        label1.image = my_img
        label1.place(x = 0, y = 0)
       
        f= ("Arial", 28, "bold")
        label1 = Label(lgn_frame1, text="Resume Screening",font=f,bg="#fc9714",fg="white")
        label1.place(x = 520, y = 10)
        
        f1= ("times", 20, "bold")
        label1 = Label(lgn_frame1, text="Upload files *",font=f1,bg="#fc9714",fg="blue")
        label1.place(x = 420, y = 90)
        
        label1 = Label(lgn_frame1, text="Enter Job Description *",font=f1,bg="#fc9714",fg="blue")
        label1.place(x = 420, y = 140)
        NameEn = Entry(lgn_frame1, textvariable=Name,width="30")
        NameEn.place(x=720,y=140)
        def open_files():
            global filez
            filez = fd.askopenfilenames(parent=lgn_frame1, title='Choose a file')
            print(filez)
        def result():
            global tree
            df=resume_scan(filez,NameEn.get())
            cols = list(df.columns)
            tree = ttk.Treeview(lgn_frame1)
            tree.place(x = 200, y = 200)
            tree["columns"] = cols
            for i in cols:
                tree.column(i, anchor="w")
                tree.heading(i, text=i, anchor='w')
            txt="We Got "+str(len(df))+" Profiles:"
            #label1 = Label(lgn_frame1, text=txt,font=f1,bg="Ivory",fg="blue")
            #label1.place(x = 420, y = 160)
            for index, row in df.iterrows():
                #tree.insert("",0,text=index,values=list(row))
                tree.insert("", "end", values=list(row))
        def clear():
            NameEn.delete(first=0,last=100)
            for item in tree.get_children():
                tree.delete(item)
        def back():
            lgn_frame1.destroy()
        
        image4=PIL.Image.open("upload.png")
        img4=image4.resize((100, 52))
        my_img=ImageTk.PhotoImage(img4)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=open_files,bd=0,bg="#fc9714",font=f1,fg='Ivory')
        open_button.image=my_img
        open_button.place(x=720,y=70)
        
        
        image1=PIL.Image.open("submit.png")
     
        img1=image1.resize((80, 50))
        my_img=ImageTk.PhotoImage(img1)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=result,bd=0,bg="#fc9714",font=f1,fg='Ivory')
        open_button.image=my_img
        open_button.place(x=920,y=130)
        
        image4=PIL.Image.open("clear.png")
        img4=image4.resize((100, 52))
        my_img=ImageTk.PhotoImage(img4)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=clear,bd=0,bg="#fc9714",font=f1,fg='Ivory')
        open_button.image=my_img
        open_button.place(x=1020,y=120)
        
        
        image=PIL.Image.open("back.png")
     
        img=image.resize((80, 80))
        my_img=ImageTk.PhotoImage(img)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=back,bd=0,bg='#fc9714')
        open_button.image = my_img
        open_button.place(x=120,y=30)
    def view_resume():
        Name=StringVar()
        lgn_frame1 = Frame(titleframe, bg='#fc9714', width=1390, height=600,highlightbackground="gray", highlightthickness=2)
        lgn_frame1.place(x=1, y=100)
       
        image4=PIL.Image.open("bg1.png")
        img4=image4.resize((1400, 700))
        my_img=ImageTk.PhotoImage(img4)
        
        label1 = Label(lgn_frame1, image = my_img)
        label1.image = my_img
        label1.place(x = 0, y = 0)
        f= ("Arial", 28, "bold")
        label1 = Label(lgn_frame1, text="Display Resume Data",font=f,bg="#fc9714",fg="white")
        label1.place(x = 520, y = 15)
        
        f1= ("Times", 18, "bold")
        label1 = Label(lgn_frame1, text="Upload file *",font=f1,bg="#fc9714",fg="blue")
        label1.place(x = 480, y = 90)
        
        def open_files():
            global filez
            filez = fd.askopenfilenames(parent=lgn_frame1, title='Choose a file')
            print(filez)
        def result():
            clearToTextInput()
            df=view(filez)
            
            #text = Text(lgn_frame1,width="50",font=f)
            data=df.values.tolist()
            text.insert(INSERT, "----------------------------------------------"+"Important Resume Data"+"--------------------------------------------------"+"\n")
            text.insert(INSERT, ""+"\n")
            for v in data:
                
                 text.insert(INSERT, "\t\t\t"+"Name"+" : "+"\t"+v[0]+"\n")
                 text.insert(INSERT, ""+"\n")
                 text.insert(INSERT, "\t\t\t"+"Mail"+" : "+"\t"+v[1]+"\n")
                 text.insert(INSERT, ""+"\n")
                 text.insert(INSERT, "\t\t\t"+"Mobile"+" : "+"\t"+v[2]+"\n")
                 text.insert(INSERT, ""+"\n")
                 text.insert(INSERT, "\t\t\t"+"Skils"+" : "+"\t"+",".join(v[3])+"\n")
        def clearToTextInput():
            text.delete("1.0","end")
        def back():
            lgn_frame1.destroy()
        f4= ("Times", 15, "bold")    
        text = Text(lgn_frame1,width="95",height="50",font=f4,bg="#faba66")
        text.place(x = 200, y = 200)
        
        image4=PIL.Image.open("upload.png")
        img4=image4.resize((100, 52))
        my_img=ImageTk.PhotoImage(img4)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=open_files,bd=0,bg="#fc9714",font=f1,fg='Ivory')
        open_button.image=my_img
        open_button.place(x=720,y=70)
        
        image1=PIL.Image.open("submit.png")
     
        img1=image1.resize((80, 50))
        my_img=ImageTk.PhotoImage(img1)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=result,bd=0,bg="#fc9714",font=f1,fg='Ivory')
        open_button.image=my_img
        
        
        open_button.place(x=620,y=140)
        
        image=PIL.Image.open("back.png")
     
        img=image.resize((80, 80))
        my_img=ImageTk.PhotoImage(img)
        open_button = Button(lgn_frame1,image=my_img,borderwidth=0,command=back,bd=0,bg='#fc9714')
        open_button.image = my_img
        open_button.place(x=120,y=30)
    def home():  
        
        image=PIL.Image.open("4.jpg")
    
        img=image.resize((1400, 700))
        my_img=ImageTk.PhotoImage(img)
                    # Show image using label
        label1 = Label( titleframe, image = my_img)
        label1.image = my_img
        label1.place(x = 0, y = 100)
    def logout():
        titleframe.destroy()
    b= ("Decary Sans", 10, "bold")
    
    image1=PIL.Image.open("home.png")
 
    img1=image1.resize((80, 50))
    my_img1=ImageTk.PhotoImage(img1)
    open_button = Button(titleframe,image=my_img1,command=home,bd=0,borderwidth=0,bg="ghost white",font=b,fg='dark blue')
    open_button.image=my_img1
    open_button.place(x=800,y=50)
    
    image2=PIL.Image.open("rs.png")
    img2=image2.resize((120, 52))
    my_img=ImageTk.PhotoImage(img2)
    open_button = Button(titleframe,image=my_img,command=resume_screen,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.image=my_img
    open_button.place(x=910,y=46)
    
    image3=PIL.Image.open("vr.png")
    img3=image3.resize((120, 52))
    my_img=ImageTk.PhotoImage(img3)
    open_button = Button(titleframe,image=my_img,command=view_resume,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.image=my_img
    open_button.place(x=1090,y=45)
    
    image4=PIL.Image.open("logout.png")
    img4=image4.resize((100, 52))
    my_img=ImageTk.PhotoImage(img4)
    open_button = Button(titleframe,image=my_img,command=logout,bd=0,bg="ghost white",font=b,fg='dark blue')
    open_button.image=my_img
    open_button.place(x=1270,y=45)



#root.mainloop()
