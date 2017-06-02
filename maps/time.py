import googlemaps,re,pytz
from datetime import datetime
from semantic.dates import DateService

gmaps = googlemaps.Client(key='AIzaSyDPubuqAlEnsPjXAdkTdFrPq4cjBLOOIZY')

now = datetime.now()

#list2 = gmaps.directions('pinglewasti,pune','katraj,pune',alternatives=True, departure_time=now)

#for n,obj in enumerate(list2):
#    print obj['summary'],obj['legs'][0]['distance']['text'],obj['legs'][0]['duration']['text']
place = 'Sochi'

geocode = gmaps.geocode(place)

lat = geocode[0]['geometry']['location']['lat']
lng = geocode[0]['geometry']['location']['lng']

time = gmaps.timezone((lat,lng),timestamp=now)
timeZone = time['timeZoneId']
tz = pytz.timezone(timeZone)
service = DateService()
response = service.convertTime(datetime.now(tz))

print response
