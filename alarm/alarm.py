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

deviceID = "250195"
firebase = pyrebase.initialize_app(config)

class Alarm():
    def __init__(self, db):
        self.db = db

    def set(self,hours, minutes):
        try:
            time = hours + ":" + minutes
            val = "1"
            self.db.child("Alarm").set({"AlarmTime": time,"Status": val})
        except:
            print "Could not set the alarm"
            return

    def delete(self):
        val="0"
        self.db.child("Alarm").update({"Status": val})
        print("Done")

while True:
     device = firebase.database().child("Devices").child(deviceID).get()
     user = device.val()["Alpha"]
     db = firebase.database().child("Users").child(user)
     text = str(raw_input())
     if text == "s":
        alarm_HH = input("Enter the hour you want to wake up at: ")
        alarm_MM = input("Enter the minute you want to wake up at: ")

        print("You want to wake up at: {0:02}:{1:02}").format(alarm_HH, alarm_MM)

        alarm = Alarm(db)
        alarm.set(str(alarm_HH),str(alarm_MM))
     elif text == "d":
        alarm = Alarm(db)
        alarm.delete()
     elif text == "e":
        break
