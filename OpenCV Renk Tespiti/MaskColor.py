from tkinter import messagebox
import cv2
import numpy as np
import pandas as pd
class MaskColor:
    def __init__(self,filename,minR,minG,minB,maxR,maxG,maxB):
        self.filename=filename 
        self.minR=minR
        self.minG=minG
        self.minB=minB
        self.maxR=maxR
        self.maxG=maxG
        self.maxB=maxB
        
    def colorDetection(self):
        try:
            img = cv2.imread(self.filename)
            rgbimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            hsv = cv2.cvtColor(rgbimg, cv2.COLOR_RGB2HSV)
            lower = np.array([int(self.minR),int(self.minG),int(self.minB)])
            upper = np.array([int(self.maxR),int(self.maxG),int(self.maxB)])
            mask = cv2.inRange(hsv, lower, upper)
            res=cv2.bitwise_and(img,img,mask=mask)
            cv2.imshow('mask', res)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            messagebox.showerror("Hata", "Renk Değerleri Geçersiz Karakter İçeriyor")
       

        