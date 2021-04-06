from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from tkinter import ttk
from cv2 import cv2
import sys
import numpy as np
from ColorDetect import *
from MaskColor import *
from HSVColor import *
import numpy as np
import pandas as pd
from tkinter import messagebox

class MenuGUI:
    def __init__(self):
        
        def openFileImg():
            try:
                filename=filedialog.askopenfilename(initialdir="/img/", title="Lütfen Resim ",filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png")))
                myImage.place_forget()
                imageFirst=Image.open(filename)
                imageLast=imageFirst.resize((650, 500),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=650,height=500)
                myImageLast.image=myImg
                myImageLast.place(x=50,y=145)
                head_tail = os.path.split(filename) 
                Path.config(text=head_tail[1])
                self.video=0
                self.filename=filename
            except:
                noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
                myImageLast=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=650,height=500)
                myImageLast.image=noImage
                myImageLast.place(x=50,y=145)
                head_tail = os.path.split(filename) 
                Path.config(text=head_tail[1])
                self.video=1
                self.filename=filename

        def imgDetect():
            try:
                a=ColorDetect(self.filename)
                a.colorDetection()     
                if(self.video==1):
                    imageFirst=Image.open("img/noImage.png")
                else:
                    imageFirst=Image.open("img/dist/objtest.jpg")
                imageLast=imageFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=650,height=500)
                myImageLast.image=myImg
                myImageLast.place(x=650,y=145)
            except:
                pass
        def hsvDetect():  
            try:
                minR2=minR.get("1.0","end-1c")
                minG2=minG.get("1.0","end-1c")
                minB2=minB.get("1.0","end-1c")
                maxR2=maxR.get("1.0","end-1c")
                maxG2=maxG.get("1.0","end-1c")
                maxB2=maxB.get("1.0","end-1c")
                a=HSVColor(self.filename,minR2,minG2,minB2,maxR2,maxG2,maxB2)
                a.colorDetection()  
            except:
                messagebox.showerror("Hata", "Resmi ve Rengi Seçtiğinizden Emin Olunuz")     
        def maskDetect():
            try:
                minR2=minR.get("1.0","end-1c")
                minG2=minG.get("1.0","end-1c")
                minB2=minB.get("1.0","end-1c")
                maxR2=maxR.get("1.0","end-1c")
                maxG2=maxG.get("1.0","end-1c")
                maxB2=maxB.get("1.0","end-1c")
                a=MaskColor(self.filename,minR2,minG2,minB2,maxR2,maxG2,maxB2)
                a.colorDetection()    
           
            except:
                messagebox.showerror("Hata", "Resmi ve Rengi Seçtiğinizden Emin Olunuz")    
            
    #<---Form Ayarları--->

        self.root = Tk()
        self.root.wm_iconbitmap('img/iconum.ico')
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366,768)
        self.root.title("OpenCV İle Renk Tespiti")
        self.root.configure(background='#0075d5')
        
    #</---Form Ayarları--->


    #<---Resimlerin Eklenmesi--->


        find=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\search.png"))
        noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
        fotoImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\foto.png"))
        maskImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\video.png"))
        hsvImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\hsv.png"))

    #</---Resimlerin Eklenmesi--->
    #<---Combobox Oluşturulması--->
        n = StringVar()
        index=["Color","minR","minG","minB","maxR","maxG","maxB"]
        self.csv = pd.read_csv('dataset/mycolors.csv', names=index)
        colors=self.csv.Color.to_list()  
        colorCombobox = ttk.Combobox(self.root, width = 27, textvariable = n) 
        colorCombobox['values'] = colors
        colorCombobox.place(x=860,y=150)
        colorCombobox.current() 
        def select():
            value = colorCombobox.get()
            for i in range(len(self.csv)):
                if( value == self.csv.loc[i,"Color"]) :
                    minR.delete(1.0,END)
                    minG.delete(1.0,END)
                    minB.delete(1.0,END)
                    maxR.delete(1.0,END)
                    maxG.delete(1.0,END)
                    maxB.delete(1.0,END)
                    minR.insert(INSERT,self.csv.loc[i,"minR"])
                    minG.insert(INSERT,self.csv.loc[i,"minG"])
                    minB.insert(INSERT,self.csv.loc[i,"minB"])
                    maxR.insert(INSERT,self.csv.loc[i,"maxR"])
                    maxG.insert(INSERT,self.csv.loc[i,"maxG"])
                    maxB.insert(INSERT,self.csv.loc[i,"maxB"])
            
        
        
         
    #</---Combobox Oluşturulması--->
    #<---Butonların Oluşturulması--->

      
        goButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=select,width=24,height=24,bg="#0075d5",fg="#000000")
        goButton.image=find
        goButton.place(x=1050,y=150)

        findButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=openFileImg,width=24,height=24,bg="#0075d5",fg="#000000")
        findButton.image=find
        findButton.place(x=680,y=100)

        imageButton=Button(self.root,image=fotoImage,bd=0,highlightthickness=0,command=imgDetect,bg="#0075d5",fg="#ffffff")
        imageButton.image=fotoImage
        imageButton.place(x=780,y=450)

        maskButton=Button(self.root,image=maskImage,bd=0,highlightthickness=0,command=maskDetect,bg="#0075d5",fg="#000000")
        maskButton.image=maskImage
        maskButton.place(x=780,y=230)

        hsvButton=Button(self.root,image=hsvImage,bd=0,highlightthickness=0,command=hsvDetect,bg="#0075d5",fg="#000000")
        hsvButton.image=hsvImage
        hsvButton.place(x=780,y=340)
    

    #</---Butonların Oluşturulması--->

      



    #<---Textboxların Oluşturulması--->

        minR = Text(self.root, fg="#0075d5",bg="#ffffff",width=4,height=1)

        minG = Text(self.root, fg="#0075d5",bg="#ffffff",width=4,height=1)

        minB = Text(self.root, fg="#0075d5",bg="#ffffff",width=4,height=1)

        maxR = Text(self.root, fg="#0075d5",bg="#ffffff",width=4,height=1)

        maxG = Text(self.root, fg="#0075d5",bg="#ffffff",width=4,height=1)

        maxB = Text(self.root, fg="#0075d5",bg="#ffffff",width=4,height=1)
    #</---Textboxların Oluşturulması--->

    #<---CheckBoxların Oluşturulması--->
        def kontrolCheck():
            if(var1.get()==1):
                minR.place(x=860,y=195)
                minG.place(x=900,y=195)
                minB.place(x=940,y=195)
                maxR.place(x=860,y=225)
                maxG.place(x=900,y=225)
                maxB.place(x=940,y=225)
                minRGB.place(x=780,y=195)
                maxRGB.place(x=780,y=225)
                imageButton.place(x=780,y=530)
                maskButton.place(x=780,y=310)
                hsvButton.place(x=780,y=420)

            else:
                minR.place_forget()
                minG.place_forget()
                minB.place_forget()
                maxR.place_forget()
                maxG.place_forget()
                maxB.place_forget()
                minRGB.place_forget()
                maxRGB.place_forget()
                imageButton.place(x=780,y=450)
                maskButton.place(x=780,y=230)
                hsvButton.place(x=780,y=340)
        var1=IntVar()
        checkBox=Checkbutton(self.root,text="Ayarlar",variable=var1,fg='#ffffff',bg='#0075d5',command=kontrolCheck)
        checkBox.place(x=1074,y=150)

    #</---CheckBoxların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="OpenCV ile Renk Tespiti",font = "Arial 12 bold ",bg="#0075d5",fg="#ffffff")
        title.place(x=563,y=30)

        fileLbl=Label(self.root,text="Dosya Adı:",bg="#0075d5",fg="#ffffff")
        fileLbl.place(x=55,y=100)

        colorLbl=Label(self.root,text=" Renk Seçin :",bg="#0075d5",fg="#ffffff")
        colorLbl.place(x=780,y=150)

        minRGB=Label(self.root,text="min HSV:",bg="#0075d5",fg="#ffffff")
       

        maxRGB=Label(self.root,text="max HSV:",bg="#0075d5",fg="#ffffff")
        

        Path=Label(self.root,text="Lütfen Dosyayı Seçiniz ...",bg="#0075d5",fg="#ffffff")
        Path.place(x=160,y=100)
        
        myImage=Label(self.root,image=noImage,bg="#0075d5",fg="#ffffff",width=650,height=500)
        myImage.place(x=50,y=145)

    

        description=Label(self.root,text="Açılan Pencereyi Kapatmak İçin ESC ye Basınız",bg="#0075d5",fg="#ffffff")
        description.place(x=50,y=670)

    #</---Labellerın Oluşturulması--->


        self.root.mainloop()
    
    #<---Fonksiyonların Tanımlanması--->
    
  
 
  
    def Quit(self):
        self.root.destroy()

    #</---Fonksiyonların Tanımlanması--->


   