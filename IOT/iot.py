import pyrebase
import time,re

config = {
    "apiKey": "AIzaSyDNRB7slEjDKppE9shSqL6_FHUDenUL-ec",
    "authDomain": "arckinfinal.firebaseapp.com",
    "databaseURL": "https://arckinfinal.firebaseio.com",
    "projectId": "arckinfinal",
    "storageBucket": "arckinfinal.appspot.com"
}

deviceID = "1"
firebase = pyrebase.initialize_app(config)

class IoT():
    def __init__(self, db):
        self.db = db

    def drapes(self,cnt):
        try:
            self.db.child("Curtains").update({"Switch": cnt})
            return "Done"
        except:
            print "Try Again"
            return

    def lSwitch(self,cnt):
         try:
             self.db.child("LCDDisplay").update({"switch":cnt})
             return "Done"
         except:
             print "Try Again"
             return

    def lights(self,cnt):
        try:
            self.db.child("LEDLights").update({"Switch": cnt})
            return "Done"
        except:
            print "Try Again"
            return

    def moods(self,mood):
        try:
            self.db.child("LEDLights").update({"moods": mood})
            return "Done"
        except:
            print "Try Again"
            return
    def lDisplay(self):
#        try:
        dis = raw_input("Enter the text to display")
        self.db.child("LCDDisplay").update({"text": dis})
        print "Done"
#        except:
#            print "Try again"
#            return


def doSomethingElse():
    pass

db = firebase.database().child("IoTBox").child(deviceID)

iot = IoT(db)
functions = {"light","drape","curtain","lcd","tv","mood","color",
            "television"}

controls = {"on":"1","off":"0","open":"1","close":"0","roman":"1",
           "relax":"2","peace":"3","work":"4","red":"1","blue":"2",
           "green":"3","yellow":"4","power on":"1","power off":"0"}

while True:
     db = firebase.database().child("IoTBox").child(deviceID)
     iot = IoT(db)
     text = str(raw_input("Enter: "))
     funcs = re.findall("|".join(functions),text)
     for i in funcs:
         if i == "light":
             op = re.search(r"\bon\b|\boff\b",text).group()
             cnt = controls.get(op, doSomethingElse())
             liop = iot.lights(cnt)
             print liop
         elif i in ["drape","curtain"]:
             op = re.search(r"\bopen\b|\bclose\b",text).group()
             cnt = controls.get(op, doSomethingElse())
             drop = iot.drapes(cnt)
             print drop
         elif i in ["mood","color"]:
             op = re.search(r"roman|red|relax|blue|peace|green|yellow|work",text,re.M|re.I).group()
             cnt = controls.get(op, doSomethingElse())
             drop = iot.moods(cnt)
             print drop
         elif i in ['tv',"television","lcd"]:
             try:
                 op = re.search(r"\bpower on\b|\bpower off\b",text,re.I).group()
                 cnt = controls.get(op, doSomethingElse())
             except:
                 iot.lDisplay()
