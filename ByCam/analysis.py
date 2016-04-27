#!/usr/bin/env python
# -*- coding: utf-8 -*-
#By Wangchunshan

#設定檔輸入
import sys
sys.path.append("./lib/")
import SQL
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
import analysis_ui_set as uiset

def post():
        try:
                SQL.clear('detect')
                SQL.copyttodetect('tem')
                SQL.clear('tem')
                print 'reset success'
        except:
                print 'reset error'
if __name__ == '__main__':
    '''
    顯示選擇表單來選擇目標日期並觸發後續分析
    '''

    
    #開啟GUI
    app = analysis_select_ui.QtGui.QApplication(sys.argv) #
    window = uiset.MainWindow()
    window.show()
    app.exec_()
    

    
    post()
    cv2.destroyAllWindows()
