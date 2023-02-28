import datetime
from playsound import playsound
import time

class AlarmClock():
    def setAlarm(self):
       hh=input("Set Hour   :")
       mm=input("Set Minute :")
      
       alarm_time= hh+mm 
       return alarm_time
    def setRingtone(self):
       File_Address=input("Enter ringtone address ") 
       return File_Address
    def setDays(self):
         alarm_days=[]
         while True:
           alarm_days.append(input("Day on which you want alarm ;(formate is sun  mon tue ...)"))
           if 'break' in alarm_days: break
         return alarm_days
    def Ringing(self,time,addressFile,*alarmDays):
      days=['mon','tue','wed','thu','fri','sat','sun']
      day_index=datetime.datetime.now().weekday()
      tt=datetime.datetime.now()
      alarmTime = str(tt.hour) + str(tt.minute) 
      if (days[day_index]  in alarmDays[0] ):
          if(alarmTime==time):
             playsound(addressFile)
             
       


user=AlarmClock()
time=user.setAlarm()
add=user.setRingtone()
al_day=user.setDays()
 
while True:
   user.Ringing(time,add,al_day)

 

