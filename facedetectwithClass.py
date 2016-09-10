#!/usr/bin/env python

import numpy as np
import cv2
import cv2.cv as cv
from video import create_capture
from common import clock, draw_str

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''
class PicData:
	def __init__(self,pic,cascade):		
		gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
		gray = cv2.equalizeHist(gray)
		self.SourcePic = pic
		self.GrayPic = gray
		self.Cascade = cascade		
		self.rects = self.detect(self.GrayPic, self.Cascade)
		self.DrawPic=self.draw_rects(self.SourcePic,self.rects, (0, 255, 0))
		self.PeopleNum = len(self.rects)
	
	def detect(self,img, cascade):
		rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
		if len(rects) == 0:
		    return []
		rects[:,2:] += rects[:,:2]
		return rects

	def draw_rects(self,img, rects, color):
		for x1, y1, x2, y2 in rects:
		    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
		return img

if __name__ == '__main__':
    import sys, getopt
    print help_message

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "../../data/haarcascades/haarcascade_frontalface_alt.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)

    cam = create_capture(video_src, fallback='synth:bg=../cpp/lena.jpg:noise=0.05')

    while True:
		ret, img = cam.read()

		vis = PicData(img,cascade)
		#print type(img)
		#print type(vis)
		cv2.imshow('facedetect', vis.DrawPic)
		print vis.PeopleNum
		if 0xFF & cv2.waitKey(5) == 27:
			break
    cv2.destroyAllWindows()
