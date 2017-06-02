import requests,json

list = []

def display(train,arr,dep):
    for i in trains:
        if str(i["dest_arrival_time"]) < str(arr) and str(i["src_departure_time"]) > str(dep):
            list.append(i)

    for i in list:
        print "Train No: ", i["number"], ";origin: ", i["from"]["name"],\
              ";src dep time: ", i["src_departure_time"],";des arr time: ", i["dest_arrival_time"],\
              ";des: ", i["to"]["name"],";airline: ",";Train name: ", i["name"],"\n"

def stationCode(src,des):
    srcUrl = "http://api.railwayapi.com/suggest_station/name/"+ src +"/apikey/n4l8l6fc/"
    destUrl = "http://api.railwayapi.com/suggest_station/name/"+ dest + "/apikey/n4l8l6fc/"

    srcRes = requests.get(srcUrl)
    destRes = requests.get(destUrl)

    srcData = srcRes.json()["station"][0]["code"]
    destData = destRes.json()["station"][0]["code"]
    return srcData, destData

key = "n4l8l6fc"

src = raw_input("Source Station: ")
dest = raw_input("Destination Station: ")

srcCode,destCode = stationCode(src,dest)

date = "16-07"

url = "http://api.railwayapi.com/between/source/"+ srcCode + "/dest/"+ destCode +"/date/"+ date +"/apikey/"+ key

response = requests.get(url)
data = response.json()

trains = data["train"]

#display(src,des,date,trains)
sort = raw_input("Sort by: ")

if sort == "1":
    arr = raw_input("arr time: ")
    dep = raw_input("dep time: ")
    #print arr, dep
    display(trains,arr,dep)
elif sort == "2":
    arr = raw_input("arr time: ")
    dep = "00:00"
    display(trains,arr,dep)
elif sort == "3":
    dep = raw_input("dep time: ")
    arr = "23:59"
    display(trains,arr,dep)
elif sort == "0":
    dep = "00:00"
    arr =  "23:59"
    display(trains,arr,dep)
