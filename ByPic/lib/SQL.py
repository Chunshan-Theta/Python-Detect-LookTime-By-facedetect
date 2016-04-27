# -*- coding: cp950 -*-
import config 
import datetime

#方法：查詢資料庫目前總比數    
def catchidnum():
    try:
        cursor = config.db.cursor() 
        cursor.execute("Select Count(*) FROM `%s`" % ('detect'))
        index = cursor.fetchall()
        config.db.commit()
        cursor.close()
        return index[0][0] or 0
    except:
        print 'fun: catchidnum() error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
        return 0
#方法：抓取資料庫中單筆資料    
def catchdbfetch(sqlid):
    try:
        cursor = config.db.cursor()
        cursor.execute("SELECT * FROM `detect` WHERE `id` = %s"%(str(sqlid)))
        result_sx1 = cursor.fetchall()    
        config.db.commit()
        cursor.close()
        return result_sx1
    except:
        print 'fun:catchdbfetch error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
        return 0

# def catchdbfetchs(sqlid):
    # try:
        # cursor = config.db.cursor()
        # cursor.execute("SELECT * FROM `%s` WHERE `id` = %s"%('detect',str(sqlid)))
        # result_sx1 = cursor.fetchall()    
        # config.db.commit()    
        # cursor.close()
        # return result_sx1
    # except:
        # print 'fun:catchdbfetchs error'
        # nowtime = datetime.datetime.now()
        # print str(nowtime)
        # return 0
def sql_exe(Tdb,Tcursor,TSQL):
    try:
        Tcursor.execute(TSQL)
        result = Tcursor.fetchall()
        Tdb.commit()    
        cursor.close()
    except:
        print 'fun:sql_exe error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
def updatef(data,pnum,fid):
    try:
        SQL = "UPDATE `%s` SET `count` = '%s' WHERE `id` = '%s';" % (data,pnum,fid)
        cursor = config.db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        config.db.commit()
        print '!!Notic: !!! update data of SQL'        
        cursor.close()
    except:
        print 'fun:insertpythondetect error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
def insertpythondetect(savedir,savepicid,pnum):
    try:
        SQL = "INSERT INTO `detect` (`id`, `time`, `dir`, `count`) VALUES (%f, CURRENT_TIMESTAMP, '%s', %f);" % (savepicid,savedir,pnum)
        cursor = config.db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        config.db.commit()
        print '!!Notic: !!! Insert pic data into SQL'        
        cursor.close()
    except:
        print 'fun:insertpythondetect error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
def insertpythondetect_frompic(savedir,savepicid,pnum):
    try:
        time = datetime.datetime(2000,05,11,00,00,00,00)+ datetime.timedelta(seconds=catchidnum())
        #time = datetime.datetime.now()
        SQL = "INSERT INTO `detect` (`id`, `time`, `dir`, `count`) VALUES (%f, '%s', '%s', %f);" % (savepicid,str(time),savedir,pnum)
        cursor = config.db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        config.db.commit()
        print 'Insert pic data into SQL'                
        cursor.close()
    except:
        print 'fun:insertpythondetect_frompic error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
def updatapythondetect(facecount,sqlid):
    try:
        sql="UPDATE `detect` SET `count` = '%0.0f' WHERE `detect`.`id` = %0.0f;"%(facecount,sqlid)
        cursor = config.db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        config.db.commit()        
        cursor.close()
    except:
        print 'fun:updatapythondetect error'
        nowtime = datetime.datetime.now()
        print str(nowtime)
def newlist(name):
        #建立新資料表：CREATE TABLE new_table LIKE old_db.old_table;

        #複製資料：INSERT new_table SELECT * FROM old_db.old_table;
        SQL = "CREATE TABLE `%s` LIKE `detect`"%(name)
        cursor = config.db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        config.db.commit()
        print '!!Notic: !!! 開啟新資料表:'+str(name)    
        cursor.close()

        
def copytonewlist(name):

        '''
        將主資料表所有資料轉至暫存資料表
        '''
        #建立新資料表：CREATE TABLE new_table LIKE old_db.old_table;

        #複製資料：INSERT new_table SELECT * FROM old_db.old_table;
        SQL = "INSERT `%s` SELECT * FROM `detect`"%(name)
        cursor = config.db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        config.db.commit()
        #print '!!Notic: !!! 轉至資料至:'+str(name)         
        cursor.close()
def copyttodetect(name):
        '''
        
        將要分析之資料表轉至主資料表
        '''
        try:
            SQL = "INSERT `detect` SELECT * FROM `%s`"%(name)
            cursor = config.db.cursor()
            cursor.execute(SQL)    
            result = cursor.fetchall()
            config.db.commit()
            #print '!!Notic: !!!'+str(name)+' 轉至資料至 `detect`'         
            cursor.close()
        except:
            print 'copyttodetect error'
def tables():
        SQL ="show tables from `%s`"%(config.dbname)
        cursor = config.db.cursor() 
        cursor.execute(SQL)
        index = cursor.fetchall()
        config.db.commit()
        cursor.close()
        return index
def clear(name):
    try:
        SQL = "TRUNCATE TABLE `%s`"%(name)
        cursor = config.db.cursor()
        cursor.execute(SQL)    
        result = cursor.fetchall()
        config.db.commit()
        #print '!!Notic: !!! clear'        
        cursor.close()
    except:
        print 'fun: SQL clear() error'
        nowtime = datetime.datetime.now()
        print str(nowtime)

        
        
def writedocument(name,time,stime):
     try:        
         SQL = "INSERT INTO `detectdocument` (`id`, `name`, `time`,`stime`) VALUES (NULL, '%s', %f,'%s');" % (name,int(time),stime)
         cursor = config.db.cursor()
         cursor.execute(SQL)    
         result = cursor.fetchall()
         config.db.commit()
         #print '!!Notic: !!! clear'        
         cursor.close()
     except:
         print 'fun: SQL writedocument() error'
         nowtime = datetime.datetime.now()
         print str(nowtime)
        
def searchdocument(name):
     SQL = "SELECT * FROM `detectdocument` WHERE `name` = '%s'" % (name)
     cursor = config.db.cursor()
     cursor.execute(SQL)    
     index = cursor.fetchall()
     config.db.commit()
     #print '!!Notic: !!! clear'        
     cursor.close()
     return index
     
        

