from collections import OrderedDict
import pyrebase,googlemaps
import time,re

config = {
    "apiKey": "AIzaSyDNRB7slEjDKppE9shSqL6_FHUDenUL-ec",
    "authDomain": "arckinfinal.firebaseapp.com",
    "databaseURL": "https://arckinfinal.firebaseio.com",
    "projectId": "arckinfinal",
    "storageBucket": "arckinfinal.appspot.com"
}

gmaps = googlemaps.Client(key='AIzaSyDPubuqAlEnsPjXAdkTdFrPq4cjBLOOIZY')

deviceID = "16"
firebase = pyrebase.initialize_app(config)

class IoT():
    def __init__(self, db):
        self.db = db

    def getAlpha(self):
        try:
            data = self.db.child("Devices").child(deviceID).get()
            print data.val()
            key = data.val()['Alpha']
            print key
            return key
        except:
            print "Try Again"
            return
    def getAdd(self,key):
        try:
            data = self.db.child('Users').child(key).child('Profile').child('address').get()
            add = data.val()
            return add
        except:
            print "Error, try again"
            return

db = firebase.database()
#data = db.child("Devices").child(deviceID)
#key1 =  data.val()['Alpha']
#print key1
iot = IoT(db)
key = iot.getAlpha()
add = iot.getAdd(key)
print add
start_geocode = gmaps.geocode(add)
slat = start_geocode[0]['geometry']['location']['lat']
slong = start_geocode[0]['geometry']['location']['lng']
print slat , slong


end_geocode = gmaps.geocode('aissms college of engineering')
elat = end_geocode[0]['geometry']['location']['lat']
elong = end_geocode[0]['geometry']['location']['lng']
print elat , elong
