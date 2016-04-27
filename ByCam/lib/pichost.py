# -*- coding: cp950 -*-
import cv2

def save(savepic,savedir):#(儲存影像,影像儲存路徑)
    
    cv2.imwrite(savedir,savepic)

    print 'Save pic into host：'+savedir

def read(savedir):#(影像路徑)    
    

    print 'read pic from host：'+savedir
    
    return cv2.imread(savedir)
