
# -*- coding: cp950 -*-
import MySQLdb
import datetime
import os
import MySQLdb
#----------------------------------------------------------
#---��
facedetect = '����esc�����{��' #�v�������W��(�w�]�ȡG'facedetect')    
WT = 1 #�ɶ����j(�w�]�ȡG1000 = 1��)
db = MySQLdb.connect(host="localhost", user="theta", passwd="theta", db="test3")
dbname="test3"
#db = MySQLdb.connect(host="106.188.234.191", user="theta_host", passwd="!F40241124", db="theta_python")
#dbname="theta_python"

savedir = './image/'#�x�s���|(�w�]�ȡG'./image/screen/')
savetype = 'jpg' #�x�s�ɫ�(�w�]�ȡG'jpg')
savename = 'source' #�x�s�ɦW(�w�]�ȡG'sourcr')
saveintervaltime = datetime.timedelta(0, 1, 0)#�I�϶��j�ɶ��A�w�]�Gdatetime.timedelta(0, 1, 0)���C�@���j�ܦh�u�|�x�s�@���Ӥ�)(day,second,milliseconds)
countdownintervaltime= datetime.timedelta(0, 3, 0)#���ݳB�z�A�w�]�Gdatetime.timedelta(0, 3, 0)��T��L�H�[�ݮɶi�J�ݾ����A�A����U��������H�y���e���|�����Ӥ�)(day,second,milliseconds)
nowtime=datetime.datetime.now().strftime('%Y-%m-%d')
#---��        
#----------------------------------------------------------
def ClearMainDetect():#�M�ťD��ƪ�
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
        
newfolder=nowtime #�w�p���ͪ���Ƨ��W�٬�������
ROOT = savedir  #�T�w����X���|
newpath = os.path.join(ROOT, newfolder)
if not os.path.exists(newpath): #�b�o��IF�d��, �T�w�S���P�W���ɮצA�إ�
    os.makedirs(newpath)
    ClearMainDetect()#�Y�гy�s��Ƨ��h�P�w���s���g���A�ҥH�N�¦���ƲM��
savedir += newfolder+"/"
#print savedir


#000webhost
# $mysql_host = "mysql5.000webhost.com";
# $mysql_database = "a4269768_python";
# $mysql_user = "a4269768_theta";
# $mysql_password = "2015theta";

