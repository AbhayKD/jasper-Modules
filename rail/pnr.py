import requests,json

list = []

def display(data):
    print "Chart prpepared: ", data["chart_prepared"], ";class: ", i["class"],\

    if len(data["passengers"]) == 0:
        print "No status found"
    else:
        for i in data["passengers"]:
            print "No.:", i["no"],";Current Status",i["current_status"]


key = "n4l8l6fc"

pnr = "8259167648"

url = "http://api.railwayapi.com/pnr_status/pnr/"+ pnr +"/apikey/"+ key
response = requests.get("https://indianrailways.p.mashape.com/index.php?pnr=8259167648",
  headers={
    "X-Mashape-Key": "nCBrQf8u56mshw2fE3Eqvv63zw7Up1sUbSejsnWLiZ8pldIkXi",
    "Accept": "application/json"
  }
)
#response = requests.get(url)
data = response.json()
print "Waiting list 32"
#display(data)

