# --------------------by Wang Chunshan

# ����]�w�ɮסA�W�[�t��Library���| �bimport�]�w��
import sys
sys.path.append("./lib/")
import config
import SQL
import pichost
import catchface
import MySQLdb
import numpy as np
import cv2
import datetime
import os
# local modules
from video import create_capture
from common import clock, draw_str
# global
global lastsavecount
global countdownhandle
global startday
global starttime
global newSQLlistname
from PyQt4 import QtCore, QtGui
import analysis_select_ui
from analysis_select_ui import Ui_MainWindow as select_Ui_MainWindow #
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore, QtGui 
import sip


global piccount


#��k�G�x�s�Ϲ�
def savepic(savepic,savepicid,pnum):#(�x�s�v��,�v���s��,�x�s���|)
    #�Y�Ϥ��H�Ƭ�0�h�N��i�J�`�����ݳB�z
    if pnum != 0:
    #�p�����`�x�s�{��(�D�i�J�`�����ݳB�z)�ɡA���O���T�w����x�s���\��A�i�J�P�w�O�_���s�x�s�Ϲ�
        
        #��s�{�b�ɶ�
        nowtime = datetime.datetime.now()
        datename = datetime.datetime.now().strftime('%Y-%m-%d')
        
        #�T�{���j�ɶ�
        saveintervaltime =  9
        f=SQL.catchdbfetch(SQL.catchidnum())
        
        
        #Ū���W���x�s�ɶ�
        global lastsavecount
        global piccount
        if SQL.catchidnum()==0:
            print '�Ĥ@�����'
        #�Y�W���x�s�ɶ��ܤ��w�W�L"�Ϲ��x�s���j�ɶ�"�A�h�i�J����i�J�x�s�{�ǡA��������h���X
        elif (piccount-lastsavecount)<saveintervaltime :
            if int(pnum) > int(f[0][3]):
                '''
                print piccount
                print lastsavecount
                print '�{�b���'+str(pnum)
                print 'id: '+str(SQL.catchidnum())
                print '�W���H��'+str(f[0][3])
                print '�ɶ��W�l'+str(datename)
                '''
                print '-'
                SQL.updatef(datename,pnum,SQL.catchidnum())
            return
                
            
        #��s�W���x�s�ɶ�
        lastsavecount = piccount

    #�X���x�s���|
    savedir = config.savedir+config.savename+' ('+str(savepicid)+').'+config.savetype

    #�x�s�Ϲ��ܥ�����
    pichost.save(savepic,savedir)

    #�x�s�Ϲ���SQL
    SQL.insertpythondetect_frompic(savedir,savepicid,pnum)
    
    #�}�ҭ˼ƾ���(�`�����ݳB�z)
    global countdownhandle
    countdownhandle=1
    

#��k�G�˼ƾ���
def countdown():
    #��s�{�b�ɶ�
    nowtime = datetime.datetime.now()
    
    #Ū���˼Ʈɶ����׳]�w��
    countdownintervaltime = config.countdownintervaltime#(day,second,milliseconds)   
    
    #Ū���W���x�s�ɶ�
    global lastsavecount
    
    #�Y�W���x�s�ɶ��ܤ��w�W�L"�˼Ʈɶ����׳]�w��"�A�h�i�J����i�J�x�s�{�ǡA��������h���X
    if(nowtime-lastsavecount)>countdownintervaltime:
        #�T���x�s(�]����p����h��)
        savepic(img,SQL.catchidnum()+1,0)
        savepic(img,SQL.catchidnum()+1,0)
        savepic(img,SQL.catchidnum()+1,0)
        
        #�����˼ƾ���
        global countdownhandle
        countdownhandle=0
        
        
        #��ܧ����`�����ݳB�z
        print '!!Notic: !!! �T���L�H�[��'
        
        
def leader():
    #�e�m�B�z
    
    #�]�w���s���ƪ�
    global newSQLlistname
    newSQLlistname=datetime.datetime.now().strftime('%Y-%m-%d')
    
    #�T�w���s���ƪ�s�b�P�_�A�M�w������άO�s�W
    try:
        SQL.newlist(newSQLlistname)
        print "�зs��ƪ�:"+newSQLlistname
    except:
        SQL.clear(newSQLlistname)        
        print "���s��ƪ�:"+newSQLlistname
        
    #��s�}��(���s)�{���ɶ�
    global startday
    startday = datetime.datetime.now().strftime('%d')
    global starttime
    starttime = datetime.datetime.now().strftime('%H:%M:%S')
    
    #�M���D�����L��(�D����)��T
    '''
    print str(fetchdata[0][1].day)
    print str(datetime.datetime.now().day)
    '''
    fetchdata = SQL.catchdbfetch(1)
    if  SQL.catchidnum()!=0:
        if  fetchdata[0][1].day!=datetime.datetime.now().day:
            SQL.clear('detect')
            print '�M���L�ɸ�T'
   
    #��Ʈw�x�s�s�W�Ϲ����   
    
def post(img):
    #�����B�z
    #1.�s�W�T�i�e��L�H��ƪ�    
    savepic(img,SQL.catchidnum()+1,0)
    savepic(img,SQL.catchidnum()+1,0)
    savepic(img,SQL.catchidnum()+1,0)    
    print "�y�{���`�A�ثe�ɶ���"+str(datetime.datetime.now())
    
    #2.��ܸ�Ʀܤ����ƪ�
    global newSQLlistname
    SQL.copytonewlist(newSQLlistname)
    
    #3.�N�����ɶ��g�ܤ��
    nowtime = datetime.datetime.now().strftime('%H:%M:%S')
    global starttime
    
    #��ɶ��t
    start = starttime
    end = nowtime
    start_dt = datetime.datetime(2011,1,1, int(start[:2]), int(start[3:5]), int(start[6:8]),0)
    end_dt = datetime.datetime(2011,1,1, int(end[:2]), int(end[3:5]), int(end[6:8]),0)
    diff_dt = end_dt - start_dt
    #print str(diff_dt)    
    diff_dt_s = diff_dt.seconds
    #------��ɶ��tend
    #diff_dt_s = int(str(diff_dt)[:2]*60*60+int(str(diff_dt)[3:5])*60+int(str(diff_dt)[6:8])    
    nowYMD=datetime.datetime.now().strftime('%Y-%m-%d')
    SQL.writedocument(nowYMD,int(diff_dt_s),starttime)
    #print '����ɶ�'+str(diff_dt_s)+'��'
    print '�ѪR����'
    

if __name__ == '__main__':

    # --------------------by Wang Chunshan
    #�i��e�m�B�z
    leader()

    global piccount
    piccount=0
       
    #�����˼ƾ���(���s���A)              ?!!
    global countdownhandle
    countdownhandle=0
    
    #Ū����������ɶ�
    WT = config.WT
    WT = 1 if WT <=0 else WT#���Y�ɶ��]0�H�U�h�զ�1
    
    #��s�W���x�s�Ϲ��ɶ�(���s���A)
    global lastsavecount
    lastsavecount = 0
   
    
    #
    
    # --------------------�i�J�D�`���{��
    
    for Tjpg in os.listdir("insertpic"):
        global piccount
        piccount+=1
        print ""
        print "-"+str(Tjpg)
        #��s����ɶ�
        nowday = datetime.datetime.now().strftime('%d')
        
        #���B�z
        if nowday!=startday:
            post(img)           
            reload(config)
            leader()
            
        #Ū�����Y�Ϲ�
        img = cv2.imread("insertpic/"+Tjpg)
        
        #�Ϲ��Ƕ���
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        
        
        t = clock() #?
        # --------------------by Wang Chunshan
        
        
        #�`���ɶ����j
        cv2.waitKey(WT)
        
        #�ƻs�v��
        vis = img.copy()
        
        #��������H��        
        if catchface.reboolean(img) == 1:
            peoplenum = catchface.repeoplenum(img)
            vis = catchface.draw(img)
            savepic(vis,SQL.catchidnum()+1,peoplenum)
                        
        # --------------------
       
        
        # --------------------by Wang Chunshan
        # �˼ƾ���
        '''
        if countdownhandle==1:
            countdown()
        '''
        # --------------------

        if 0xFF & cv2.waitKey(5) == 27:
            break
        
    post(img)
    cv2.destroyAllWindows()
    os.system("pause") 
    #execfile('analysis.py')
