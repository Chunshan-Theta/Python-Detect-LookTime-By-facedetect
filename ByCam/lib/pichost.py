# -*- coding: cp950 -*-
import cv2

def save(savepic,savedir):#(�x�s�v��,�v���x�s���|)
    
    cv2.imwrite(savedir,savepic)

    print 'Save pic into host�G'+savedir

def read(savedir):#(�v�����|)    
    

    print 'read pic from host�G'+savedir
    
    return cv2.imread(savedir)
