from gmaps import Timezone
from gmaps import Geocoding
from datetime import datetime
from semantic.dates import DateService
import pytz

timezone = Timezone()
geo = Geocoding()
place = raw_input("Enter the name of the place: ")
coord = geo.geocode(place)
lat = coord[0]['geometry']['location']['lat']
lng = coord[0]['geometry']['location']['lng']
print lat, lng

data = timezone.timezone(lat, lng, datetime.now())
tzId = data['timeZoneId']
tz = pytz.timezone(tzId)
time = datetime.now(tz)
service = DateService()
print service.convertTime(time)
