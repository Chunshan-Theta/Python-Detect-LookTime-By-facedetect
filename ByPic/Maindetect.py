# --------------------by Wang Chunshan

# 獲取設定檔案，增加系統Library路徑 在import設定檔
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


#方法：儲存圖像
def savepic(savepic,savepicid,pnum):#(儲存影像,影像編號,儲存路徑)
    #若圖片人數為0則代表進入循環末端處理
    if pnum != 0:
    #如為正常儲存程序(非進入循環末端處理)時，為保持固定秒數儲存的功能，進入判定是否應新儲存圖像
        
        #更新現在時間
        nowtime = datetime.datetime.now()
        datename = datetime.datetime.now().strftime('%Y-%m-%d')
        
        #確認間隔時間
        saveintervaltime =  9
        f=SQL.catchdbfetch(SQL.catchidnum())
        
        
        #讀取上次儲存時間
        global lastsavecount
        global piccount
        if SQL.catchidnum()==0:
            print '第一筆資料'
        #若上次儲存時間至今已超過"圖像儲存間隔時間"，則進入接續進入儲存程序，不滿條件則跳出
        elif (piccount-lastsavecount)<saveintervaltime :
            if int(pnum) > int(f[0][3]):
                '''
                print piccount
                print lastsavecount
                print '現在日期'+str(pnum)
                print 'id: '+str(SQL.catchidnum())
                print '上次人數'+str(f[0][3])
                print '時間名子'+str(datename)
                '''
                print '-'
                SQL.updatef(datename,pnum,SQL.catchidnum())
            return
                
            
        #更新上次儲存時間
        lastsavecount = piccount

    #合併儲存路徑
    savedir = config.savedir+config.savename+' ('+str(savepicid)+').'+config.savetype

    #儲存圖像至本機端
    pichost.save(savepic,savedir)

    #儲存圖像至SQL
    SQL.insertpythondetect_frompic(savedir,savepicid,pnum)
    
    #開啟倒數機制(循環末端處理)
    global countdownhandle
    countdownhandle=1
    

#方法：倒數機制
def countdown():
    #更新現在時間
    nowtime = datetime.datetime.now()
    
    #讀取倒數時間長度設定值
    countdownintervaltime = config.countdownintervaltime#(day,second,milliseconds)   
    
    #讀取上次儲存時間
    global lastsavecount
    
    #若上次儲存時間至今已超過"倒數時間長度設定值"，則進入接續進入儲存程序，不滿條件則跳出
    if(nowtime-lastsavecount)>countdownintervaltime:
        #三次儲存(因應後計算門閘值)
        savepic(img,SQL.catchidnum()+1,0)
        savepic(img,SQL.catchidnum()+1,0)
        savepic(img,SQL.catchidnum()+1,0)
        
        #關閉倒數機制
        global countdownhandle
        countdownhandle=0
        
        
        #顯示完成循環末端處理
        print '!!Notic: !!! 三秒內無人觀看'
        
        
def leader():
    #前置處理
    
    #設定應存放資料表
    global newSQLlistname
    newSQLlistname=datetime.datetime.now().strftime('%Y-%m-%d')
    
    #確定應存放資料表存在與否，決定做選取或是新增
    try:
        SQL.newlist(newSQLlistname)
        print "創新資料表:"+newSQLlistname
    except:
        SQL.clear(newSQLlistname)        
        print "重製資料表:"+newSQLlistname
        
    #更新開啟(重製)程式時間
    global startday
    startday = datetime.datetime.now().strftime('%d')
    global starttime
    starttime = datetime.datetime.now().strftime('%H:%M:%S')
    
    #清除主測表中過時(非今日)資訊
    '''
    print str(fetchdata[0][1].day)
    print str(datetime.datetime.now().day)
    '''
    fetchdata = SQL.catchdbfetch(1)
    if  SQL.catchidnum()!=0:
        if  fetchdata[0][1].day!=datetime.datetime.now().day:
            SQL.clear('detect')
            print '清除過時資訊'
   
    #資料庫儲存新增圖像資料   
    
def post(img):
    #結束處理
    #1.新增三張前方無人資料表    
    savepic(img,SQL.catchidnum()+1,0)
    savepic(img,SQL.catchidnum()+1,0)
    savepic(img,SQL.catchidnum()+1,0)    
    print "流程正常，目前時間為"+str(datetime.datetime.now())
    
    #2.轉至資料至今日資料表
    global newSQLlistname
    SQL.copytonewlist(newSQLlistname)
    
    #3.將紀錄時間寫至文件
    nowtime = datetime.datetime.now().strftime('%H:%M:%S')
    global starttime
    
    #兩時間差
    start = starttime
    end = nowtime
    start_dt = datetime.datetime(2011,1,1, int(start[:2]), int(start[3:5]), int(start[6:8]),0)
    end_dt = datetime.datetime(2011,1,1, int(end[:2]), int(end[3:5]), int(end[6:8]),0)
    diff_dt = end_dt - start_dt
    #print str(diff_dt)    
    diff_dt_s = diff_dt.seconds
    #------兩時間差end
    #diff_dt_s = int(str(diff_dt)[:2]*60*60+int(str(diff_dt)[3:5])*60+int(str(diff_dt)[6:8])    
    nowYMD=datetime.datetime.now().strftime('%Y-%m-%d')
    SQL.writedocument(nowYMD,int(diff_dt_s),starttime)
    #print '拍攝時間'+str(diff_dt_s)+'秒'
    print '解析結束'
    

if __name__ == '__main__':

    # --------------------by Wang Chunshan
    #進行前置處理
    leader()

    global piccount
    piccount=0
       
    #關閉倒數機制(重製狀態)              ?!!
    global countdownhandle
    countdownhandle=0
    
    #讀取偵測間格時間
    WT = config.WT
    WT = 1 if WT <=0 else WT#假若時間設0以下則調成1
    
    #更新上次儲存圖像時間(重製狀態)
    global lastsavecount
    lastsavecount = 0
   
    
    #
    
    # --------------------進入主循環程式
    
    for Tjpg in os.listdir("insertpic"):
        global piccount
        piccount+=1
        print ""
        print "-"+str(Tjpg)
        #更新今日時間
        nowday = datetime.datetime.now().strftime('%d')
        
        #跨日處理
        if nowday!=startday:
            post(img)           
            reload(config)
            leader()
            
        #讀取鏡頭圖像
        img = cv2.imread("insertpic/"+Tjpg)
        
        #圖像灰階化
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        
        
        t = clock() #?
        # --------------------by Wang Chunshan
        
        
        #循環時間間隔
        cv2.waitKey(WT)
        
        #複製影像
        vis = img.copy()
        
        #當有偵測到人時        
        if catchface.reboolean(img) == 1:
            peoplenum = catchface.repeoplenum(img)
            vis = catchface.draw(img)
            savepic(vis,SQL.catchidnum()+1,peoplenum)
                        
        # --------------------
       
        
        # --------------------by Wang Chunshan
        # 倒數機制
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
