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

deviceID = "16"
firebase = pyrebase.initialize_app(config)

class ToDo():
    def __init__(self, db):
        self.db = db

    def add(self,task):
        try:
            key = db.generate_key()
            self.db.child("toDoList").update({key:task})
        except:
            print "Could not add task"
            return

    def get(self):
        list = self.db.child("toDoList").get()
        return list


while True:
     device = firebase.database().child("Devices").child(deviceID).get()
     user = device.val()["Alpha"]
     db = firebase.database().child("Users").child(user)
     text = str(raw_input())
     if text == "a":
        task = raw_input("Enter the task to add: ")
        print("Task {} added successfully").format(task)

        todo = ToDo(db)
        todo.add(str(task))
     elif text == "g":
        todo = ToDo(db)
        list = todo.get()
        for task in list.each():
            print task.val()
     elif text == "e":
        break
