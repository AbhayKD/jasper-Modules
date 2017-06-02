"""
Use the different routes time taken to travel as the traffic module data
Scrap all of these things
"""


import urllib2
import json

# http://msdn.microsoft.com/en-us/library/hh441726.aspx
# get lat/lon data from http://itouchmap.com/latlong.html

latN = str(18.54484)
latS = str(18.529762)
lonW = str(-73.884691)
lonE = str(-73.9044971)

url = 'http://dev.virtualearth.net/REST/v1/Traffic/Incidents/'+latS+','+lonW+','+latN+','+lonE+'?key=AkJdEUKFbmAamtO5vVwBH0woPK42FLGnHDkkNy7Us8VqucJVMLuOig3QBJ5T9Gvb'
response = urllib2.urlopen(url).read()
data = json.loads(response.decode('utf8'))
resources = data['resourceSets'][0]['resources']
#print '----------------------------------------------------'
#for resourceItem in resources:
#	description = resourceItem['description']
#	print description;
#	print '----------------------------------------------------'
print response
