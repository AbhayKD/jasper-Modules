import pyrebase
import time,datetime
import subprocess,os,urllib

config = {
    "apiKey": "AIzaSyDNRB7slEjDKppE9shSqL6_FHUDenUL-ec",
    "authDomain": "arckinfinal.firebaseapp.com",
    "databaseURL": "https://arckinfinal.firebaseio.com",
    "projectId": "arckinfinal",
    "storageBucket": "arckinfinal.appspot.com"
}

firebase = pyrebase.initialize_app(config)

class Voice():
    def __init__(self,users,uname):
        self.users = users
        self.name = uname

    def getVal(self):
        for user in self.users.each():
            if (user.val()["Profile"]["name"]) == self.name:
                return user.key(),user.val()
                break
            else: continue

    def getMail(self,uval,uid):
        mailRead = []
        for n,o in enumerate(uval["VoiceMails"]):
            if self.uval["VoiceMails"][o]["Read"] == "0":
                mailRead.append(uval["VoiceMails"][o]["URL"])
                db.child("Users").child(uid).child("VoiceMails").child(o).update({"Read": "1"})
        return mailRead


Uname = "Abhay Dekate"
db = firebase.database()
storage = firebase.storage()

users = db.child("Users").get()

voiceMail = Voice(users,Uname)
userID,userVal = voiceMail.getVal()

mailRead = voiceMail.getMail(userID,userVal)

print "YOU HAVE %d UNREAD MESSAGES!!!" % len(mailRead)
print mailRead

for i,obj in enumerate(mailRead):
    url = str(obj)
    urllib.urlretrieve(url,"new.wav")
    subprocess.call(["mplayer new.wav"],shell=True)
