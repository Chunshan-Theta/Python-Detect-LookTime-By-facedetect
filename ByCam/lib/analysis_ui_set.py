#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By Wangchunshan

#設定檔輸入
import sys
sys.path.append("./lib/")
import SQL
import analysis_calculate as calculate
# system modules

import numpy as np
import cv2
from video import create_capture
from common import clock, draw_str
import MySQLdb
import datetime
#select_ui
from PyQt4 import QtCore, QtGui
import analysis_select_ui
from analysis_select_ui import Ui_MainWindow as select_Ui_MainWindow #
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore, QtGui 
#
# from PyQt4 import QtCore, QtGui
# import timeselect_ui
# from timeselect_ui import Ui_MainWindow as timeselect_ui_MainWindow #
# from PyQt4.QtGui import QMainWindow
# from PyQt4 import QtCore, QtGui 

# class MainWindow2(QMainWindow, timeselect_ui_MainWindow):
    # def __init__(self, parent=None):
        # super(MainWindow2, self).__init__(parent)
        # self.setupUi(self)
class MainWindow(QMainWindow, select_Ui_MainWindow):
    '''
    設定GUI按鍵與功能連結，由此觸發分析
    '''
    global tables
    tables = SQL.tables()
    global page
    page=0
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        givename(self,tables,page)
        
        self.button[0].clicked.connect(self.selectdate_0)
        self.button[1].clicked.connect(self.selectdate_1)
        self.button[2].clicked.connect(self.selectdate_2)
        self.button[3].clicked.connect(self.selectdate_3)
        self.button[4].clicked.connect(self.selectdate_4)
        self.button[5].clicked.connect(self.selectdate_5)
        self.button[6].clicked.connect(self.selectdate_6)
        self.button[7].clicked.connect(self.selectdate_7)
        self.button[8].clicked.connect(self.selectdate_8)
        self.button[9].clicked.connect(self.selectdate_9)
        self.nextbutton.clicked.connect(self.nexttopage)
        self.neffbutton.clicked.connect(self.nefftopage)
        global selecttimerange
        selecttimerange = self.qle.text()
        #self.nextbutton.setEnabled(False)
        

    def selectdate_0(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(0+(page*10),0,0,selecttimerange)
    def selectdate_1(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(1+(page*10),0,0,selecttimerange)
    def selectdate_2(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(2+(page*10),0,0,selecttimerange)
    def selectdate_3(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(3+(page*10),0,0,selecttimerange)
    def selectdate_4(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(4+(page*10),0,0,selecttimerange)
    def selectdate_5(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(5+(page*10),0,0,selecttimerange)
    def selectdate_6(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(6+(page*10),0,0,selecttimerange)
    def selectdate_7(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(7+(page*10),0,0,selecttimerange)
    def selectdate_8(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(8+(page*10),0,0,selecttimerange)
    def selectdate_9(self):
        global selecttimerange
        selecttimerange = self.qle.text()
        global page
        calculate.main(9+(page*10),0,0,selecttimerange)
    def nexttopage(self):
        global page
        page+=1
        givename(self,tables,page)
    def nefftopage(self):
        global page
        page-=1
        givename(self,tables,page)


                


                
                
def givename(self,tables,page):
    for x in range(0,10):
        self.button[x].setEnabled(False)
        if x > len(tables)-(page*10)-4:    
            self.button[x].setText("")            
            self.nextbutton.setEnabled(False) 
        else:
              try:                    
                  self.button[x].setText(tables[x+(page*10)][0])
                  self.button[x].setEnabled(True)
              except:
                  self.button[x].setText("")
                  self.button[x].setEnabled(False)
    if page < 1:
       self.neffbutton.setEnabled(False)
    else:
       self.neffbutton.setEnabled(True)
    if (len(tables)-(page+1)*10-4)>0 :
       self.nextbutton.setEnabled(True)


    

