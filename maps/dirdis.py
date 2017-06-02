#geoloc = gmaps.geolocate(consider_ip=True,cell_towers=True,wifi_access_points=True)
#USe this for my location

import googlemaps,re
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDPubuqAlEnsPjXAdkTdFrPq4cjBLOOIZY')

now = datetime.now()
list = gmaps.directions('pinglewasti,pune','katraj,pune',mode='driving',departure_time=now)

def linkLocation(add):
    add = re.sub(r"',*","",add)
    splitAdd = add.split()
    queryAdd = "+".join(splitAdd)
    link = "https://www.google.com/maps?saddr=My+Location&daddr=" + queryAdd
    return link


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr,'',raw_html)
    cleantext = cleantext.replace('&nbsp;',''*6)
    return cleantext


for n,obj in enumerate(list[0]['legs'][0]['steps']):
    print n,cleanhtml(obj['html_instructions'])

list2 = gmaps.directions('pinglewasti,pune','katraj,pune',alternatives=True, departure_time=now)

for n,obj in enumerate(list2):
    print obj['summary'],obj['legs'][0]['distance']['text'],obj['legs'][0]['duration']['text']


"""
//Linking to a location (No directions)
https://www.google.com/maps?q=760+West+Genesee+Street+Syracuse+NY+13204

//No starting point (User input required to generate directions).
https://www.google.com/maps?daddr=760+West+Genesee+Street+Syracuse+NY+13204

//With a set location as starting point (Automatically generates directions with no user input required).
https://www.google.com/maps?saddr=760+West+Genesee+Street+Syracuse+NY+13204&daddr=314+Avery+Avenue+Syracuse+NY+13204

//With "My Location" as starting point (Automatically generates directions with no user input required).
https://www.google.com/maps?saddr=My+Location&daddr=760+West+Genesee+Street+Syracuse+NY+13204

//Current Location to Latitude and Longitude
https://www.google.com/maps?saddr=My+Location&daddr=43.12345,-76.12345

//Query search of a Latitude and Longitude
//Also shows setting a default zoom level
https://www.google.com/maps?ll=43.12345,-76.12345&q=food&amp;z=14

//String search as destination
https://www.google.com/maps?saddr=My+Location&daddr=Pinckney+Hugo+Group
"""
