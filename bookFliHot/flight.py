from goibibo import goibiboAPI
import json,operator
import re,ast

import googlemaps,re
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDPubuqAlEnsPjXAdkTdFrPq4cjBLOOIZY')

def linkLocation(add):
    add = re.sub(r"',*","",add)
    splitAdd = add.split()
    queryAdd = "+".join(splitAdd)
    link = "https://www.google.com/maps?q=" + queryAdd
    return link


def find(city):
    ports = open("ports.py", "r")
    word_list=[city]
    obj = {}
    for line in ports:
        if re.search(r"(?i)"+'|'.join(word_list), line):
            obj = ast.literal_eval(line)
    return  obj.get("code")


GO = goibiboAPI("ef071cdd","580da79a5b52f60dd27fa9f8cfd10be5")

list = []
sorted_list = []
origin = raw_input("origin city: ")
des = raw_input("destination city: ")
origin = find(origin)
desCode = find(des)
#print origin, desCode

#DO the date input work
data = GO.FlightSearch(origin, desCode, 20170610)

flights = data["data"]["onwardflights"]


def display(arr,dep,des):
    for i in flights:
        if i["destination"] == des:
            if str(i["arrtime"]) < str(arr) and str(i["deptime"]) > str(dep):
                list.append(i)
    
    sorted_list = sorted(list, key=lambda obj: obj["fare"]["grossamount"])
    for i in sorted_list:
        print "Flight No: ", i["flightno"], ";origin: ", i["origin"],";dep time: ", i["deptime"],";arr time: ", i["arrtime"],\
              "arr date: ", i["arrdate"],";des: ", i["destination"],";airline: ", i["airline"],";class: ", i["seatingclass"],\
              ";cost: ", i["fare"]["grossamount"],"\n"



sort = raw_input("Sort by: ")

if sort == "1":
    arr = raw_input("arr time: ")
    dep = raw_input("dep time: ")
    #print arr, dep
    display(arr,dep,desCode)
elif sort == "2":
    arr = raw_input("arr time: ")
    dep = "00:00"
    display(arr,dep,desCode)
elif sort == "3":
    dep = raw_input("dep time: ")
    arr = "00:00"
    display(arr,dep,desCode)

hotel = raw_input("You want me to send hotel details")
if hotel == "1":
    area = raw_input("Area you want hotel in: ")
    query = "hotels in" + "+" +area+ "+" + des
    result = linkLocation(query)
    print result
