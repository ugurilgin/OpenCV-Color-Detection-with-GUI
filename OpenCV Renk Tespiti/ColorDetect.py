from tkinter import messagebox
import cv2
import numpy as np
import pandas as pd
class ColorDetect:
    def __init__(self,filename):
        self.filename=filename 
        
    def colorDetection(self):
        def getColorName(R,G,B):
            minimum = 10000
            for i in range(len(csv)):
                d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
                if(d<=minimum):
                    minimum = d
                    cname = csv.loc[i,"color_name"]
            return cname

        def drawFunction(event, x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                
                global b,g,r,xpos,ypos, clicked
                self.clicked = True
                self.xpos = x
                self.ypos = y
                b,g,r = self.img[y,x]
                self.b = int(b)
                self.g = int(g)
                self.r = int(r)
        try:
            self.img = cv2.imread(self.filename)
            self.clicked = False
            self.r = self.g = self.b = self.xpos = self.ypos = 0
            index=["color","color_name","hex","R","G","B"]
            csv = pd.read_csv('dataset/colors.csv', names=index, header=None)    
            cv2.namedWindow('image')
            cv2.setMouseCallback('image',drawFunction)
            while(1):
                cv2.imshow("image",self.img)
                if (self.clicked):

                    cv2.rectangle(self.img,(20,20), (750,60), (self.b,self.g,self.r), -1)
                    text = getColorName(self.r,self.g,self.b) + ' R='+ str(self.r) +  ' G='+ str(self.g) +  ' B='+ str(self.b)
                    cv2.putText(self.img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
                    if(self.r+self.g+self.b>=600):
                        cv2.putText(self.img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)        
                    self.clicked=False 
                if cv2.waitKey(20) & 0xFF ==27:
                    break
                
            cv2.destroyAllWindows()
        except:
            messagebox.showerror("Hata", "Resim Seçtiğinizden Emin Olunuz")
