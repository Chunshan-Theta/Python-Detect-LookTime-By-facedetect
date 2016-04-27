#!/usr/bin/env python
# -*- coding: cp950 -*-

# 獲取設定檔案，增加系統Library路徑 在import設定檔
import sys
sys.path.append("./lib/")


import numpy as np
import cv2

# local modules
from video import create_capture
from common import clock, draw_str



help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def reboolean(Simg):    
    import sys, getopt
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "./xml/data/haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "./xml/data/haarcascades/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)    
    nested = cv2.CascadeClassifier(nested_fn)

    ret = Simg
    img = Simg
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    t = clock()
    rects = detect(gray,cascade)
    if rects!=[]:
        return 1
    return 0
def repeoplenum(Simg):    
    import sys, getopt
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "./xml/data/haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "./xml/data/haarcascades/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)    
    nested = cv2.CascadeClassifier(nested_fn)

    ret = Simg
    img = Simg
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    t = clock()
    rects = detect(gray,cascade)
   
    return len(rects) 

def draw(Simg):   
    import sys, getopt
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "./xml/data/haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "./xml/data/haarcascades/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)    
    nested = cv2.CascadeClassifier(nested_fn)


    ret = Simg
    img = Simg
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    t = clock()
    rects = detect(gray,cascade)
    if rects!=[]:
        draw_rects(Simg, rects, (0, 255, 0))
    return Simg

    
