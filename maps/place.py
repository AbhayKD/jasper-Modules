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


import googlemaps,re
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDPubuqAlEnsPjXAdkTdFrPq4cjBLOOIZY')
now = datetime.now()

query = "burger in Koregaon park"

#places = gmaps.places_autocomplete_query(query)
places = gmaps.places(query)

def linkLocation(add):
    add = re.sub(r"',*","",add)
    splitAdd = add.split()
    queryAdd = "+".join(splitAdd)
    link = "https://www.google.com/maps?q=" + queryAdd
    return link


for obj in places['results']:
    name = obj['name']
    rate = obj['rating']
    open = obj['opening_hours']['open_now']
    add = name+" "+obj['formatted_address']
    link = linkLocation(add)
    print name,rate,open,add,"\n",link
    #print places
