import pyrebase
import datetime
import os,threading

config = {
    "apiKey": "AIzaSyDNRB7slEjDKppE9shSqL6_FHUDenUL-ec",
    "authDomain": "arckinfinal.firebaseapp.com",
    "databaseURL": "https://arckinfinal.firebaseio.com",
    "projectId": "arckinfinal",
    "storageBucket": "arckinfinal.appspot.com"
}

#key = ""
#Name = "Abhay Dekate"
firebase = pyrebase.initialize_app(config)

class Voice():
    def __init__(self,users,time,uname):
        #self.db = db
        self.users = users
        self.time = time
        self.name = uname

    def getID(self):
        for user in self.users.each():
            if (user.val()["Profile"]["name"]) == self.name:
                key = user.key()
                return key
                break
            else: continue
        #    print user.val()["Profile"]["name"]
    def sendMail(self):
        #try:
            storage.child("voiceMails/%s" % self.time).put("rooster.wav")
            url = storage.child("voiceMails/%s" % self.time).get_url(None)
            print url
            return url
        #except:
        #    print "Issue in sending the file" 

Uname = "Abhay Dekate"
db = firebase.database()
storage = firebase.storage()

users = db.child("Users").get()
t = str(datetime.datetime.now().strftime('%b%d%H%M'))

voiceMail = Voice(users,t,Uname)
userID = voiceMail.getID()
url = voiceMail.sendMail()

voiceRef = db.child("Users").child(userID).child("VoiceMails")

data = {t:{"Read": "0","URL": url}}
db.update(data)
print "Done"
