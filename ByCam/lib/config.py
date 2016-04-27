
# -*- coding: cp950 -*-
import MySQLdb
import datetime
import os
import MySQLdb
#----------------------------------------------------------
#---↓
facedetect = '長按esc結束程式' #影像視窗名稱(預設值：'facedetect')    
WT = 1 #時間間隔(預設值：1000 = 1秒)
db = MySQLdb.connect(host="localhost", user="theta", passwd="theta", db="test3")
dbname="test3"
#db = MySQLdb.connect(host="106.188.234.191", user="theta_host", passwd="!F40241124", db="theta_python")
#dbname="theta_python"

savedir = './image/'#儲存路徑(預設值：'./image/screen/')
savetype = 'jpg' #儲存檔型(預設值：'jpg')
savename = 'source' #儲存檔名(預設值：'sourcr')
saveintervaltime = datetime.timedelta(0, 1, 0)#截圖間隔時間，預設：datetime.timedelta(0, 1, 0)為每一秒間隔至多只會儲存一次照片)(day,second,milliseconds)
countdownintervaltime= datetime.timedelta(0, 3, 0)#末端處理，預設：datetime.timedelta(0, 3, 0)當三秒無人觀看時進入待機狀態，直到下次偵測到人臉之前不會紀錄照片)(day,second,milliseconds)
nowtime=datetime.datetime.now().strftime('%Y-%m-%d')
#---↑        
#----------------------------------------------------------
def ClearMainDetect():#清空主資料表
    try:
        SQL = "TRUNCATE TABLE `detect`"
        cursor = db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        db.commit()
        #print '!!Notic: !!! clear'        
        cursor.close()
    except:
        print 'fun: clear error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
        
newfolder=nowtime #預計產生的資料夾名稱為今日日期
ROOT = savedir  #固定的輸出路徑
newpath = os.path.join(ROOT, newfolder)
if not os.path.exists(newpath): #在這做IF查詢, 確定沒有同名的檔案再建立
    os.makedirs(newpath)
    ClearMainDetect()#若創造新資料夾則判定為新的週期，所以將舊有資料清空
savedir += newfolder+"/"
#print savedir


#000webhost
# $mysql_host = "mysql5.000webhost.com";
# $mysql_database = "a4269768_python";
# $mysql_user = "a4269768_theta";
# $mysql_password = "2015theta";

