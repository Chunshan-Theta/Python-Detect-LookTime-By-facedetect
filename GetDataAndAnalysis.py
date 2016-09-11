import requests as rq
import json
import math
import datetime as DT



class JsonAnalysis:
    def __init__(self,Json):
        self.Json = Json
        self.StartTime = DT.datetime(int(str(Json[0]['Time'])[0:4]),int(str(Json[0]['Time'])[5:7]),int(str(Json[0]['Time'])[8:10]),int(str(Json[0]['Time'])[11:13]),int(str(Json[0]['Time'])[14:16]),int(str(Json[0]['Time'])[17:19]))
        self.EndTime = DT.datetime(int(str(Json[int(len(Json)-1)]['Time'])[0:4]),int(str(Json[int(len(Json)-1)]['Time'])[5:7]),int(str(Json[int(len(Json)-1)]['Time'])[8:10]),int(str(Json[int(len(Json)-1)]['Time'])[11:13]),int(str(Json[int(len(Json)-1)]['Time'])[14:16]),int(str(Json[int(len(Json)-1)]['Time'])[17:19]))
        self.FPeopleStream,self.PeopleStream = self.NormalizationData(self.Json)
        self.PeopleNum=self.GetNumPeople(self.FPeopleStream)
        self.DDTime =(self.EndTime-self.StartTime).seconds
        self.SumFace=self.GetSumFace(self.FPeopleStream)
        self.SumAttention=self.SumFace*self.DDTime/len(self.FPeopleStream)
        self.AverageAttention=float(self.SumAttention/self.PeopleNum)
 
    def NormalizationData(self,SourceJson):       
        PeopleStream=[]
        FPeopleStream=[]
        NowTime = str(SourceJson[0]['Time'])
        
        for i in range(len(SourceJson)):                
            PeopleStream.append(int(SourceJson[i-1]['PeopleNum']))
            NowTime = str(SourceJson[i-1]['Time'])
        for i in range(len(SourceJson)-1):                
            FPeopleStream.append(int(math.ceil(float(int(SourceJson[i-1]['PeopleNum'])+int(SourceJson[i]['PeopleNum'])+int(SourceJson[i+1]['PeopleNum']))/3)))
            NowTime = str(SourceJson[i-1]['Time'])
                
        return FPeopleStream,PeopleStream
    def GetNumPeople(self,stream):
        Num=0
        for i in range(len(stream)):
            Num+=abs(stream[i]-stream[i-1])
            
        return int(math.ceil(float(Num/2)))
    def GetSumFace(self,stream):
        Num=0
        for i in stream:
            Num+=i
            
        return Num







r = rq.post("http://IP/pi/SQLAPI.php",data={"action":"SearchSql","StartTime":"20160910000000","EndTime":"20160920000000"})
print r.status_code,r.reason
Data = json.loads(r.text)
print  type (Data)
print JsonAnalysis(Data).FPeopleStream
print "--------------------"
print JsonAnalysis(Data).SumFace
print JsonAnalysis(Data).AverageAttention




    
