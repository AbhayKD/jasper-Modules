import pyrebase
import time
import os,threading

config = {
    "apiKey": "AIzaSyDNRB7slEjDKppE9shSqL6_FHUDenUL-ec",
    "authDomain": "arckinfinal.firebaseapp.com",
    "databaseURL": "https://arckinfinal.firebaseio.com",
    "projectId": "arckinfinal",
    "storageBucket": "arckinfinal.appspot.com"
}

deviceID = "1"
firebase = pyrebase.initialize_app(config)

class Alarm():
    def __init__(self,alarmTime,status):
        #self.db = db
        self.alarm = alarmTime
        self.status = status

    def check(self):
        try:
            hours = int(self.alarm.split(':')[0])
            minutes = int(self.alarm.split(':')[1])
            now = time.localtime()
            if(now.tm_hour == hours and now.tm_min == minutes): return 1
            else: return 0
        except:
            print "Exception"
    def postpone(self):
        a = time.time()
        addTime =  str(time.localtime((a + 60*5)).tm_hour)+ ":" + str(time.localtime((a + 60*5)).tm_min)
        return addTime

device = firebase.database().child("Devices").child(deviceID).get()
user = device.val()["Alpha"]
alarmRef = firebase.database().child("Users").child(user).child("Alarm").get()

alarmTime = alarmRef.val()["AlarmTime"]
status = alarmRef.val()["Status"]

alarm = Alarm(alarmTime,status)
result = alarm.check()

if result == 1:
    print("ALARM NOW!")
    for i in range(3):
        os.system("mplayer rooster.wav")
        time.sleep(2.3)
        i += 1
    ref = firebase.database().child("Users").child(user).child("Alarm")
    ref.update({"AlarmTime": alarm.postpone(),"Status": "1"})
else:
    print "Nothing"
    a = time.time()
    addTime =  time.localtime((a + 60*5)).tm_hour,":",time.localtime((a + 60*5)).tm_min
