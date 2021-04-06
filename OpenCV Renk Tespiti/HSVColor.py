from tkinter import messagebox
import cv2
import numpy as np
import pandas as pd
class HSVColor:
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
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower = np.array([int(self.minR),int(self.minG),int(self.minB)])
            upper = np.array([int(self.maxR),int(self.maxG),int(self.maxB)])
            mask = cv2.inRange(hsv, lower, upper)
            cv2.imshow('mask', mask)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            messagebox.showerror("Hata", "Renk Değerleri Geçersiz Karakter İçeriyor")
       

                