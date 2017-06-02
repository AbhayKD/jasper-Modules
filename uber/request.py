import yaml,json
from collections import OrderedDict
import pyrebase,googlemaps
from uber_rides.client import UberRidesClient
from uber_rides.session import OAuth2Credential
from uber_rides.session import Session
from uber_rides.auth import AuthorizationCodeGrant
from uber_rides.client import UberRidesClient
from uber_rides.errors import ClientError
from uber_rides.errors import ServerError
from uber_rides.errors import UberIllegalState

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

CREDENTIALS_FILENAME = 'example/config.yaml'

STORAGE_FILENAME = 'example/oauth2_session_store.yaml'

class IoT():
    def __init__(self, db):
        self.db = db

    def getAlpha(self,deviceID):
        try:
            data = self.db.child("Devices").child(deviceID).get()
            key = data.val()['Alpha']
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
    def setRideKey(self,id,key):
        try:
         data = self.db.child('Users').child(key).child('Uber').set({"id":str(id)})
         print "Success"
        except:
            print "Error, try again"
            return

def import_app_credentials(filenam=CREDENTIALS_FILENAME):
    with open(filename,'r') as f:
        doc = yaml.load(f)

    auth_flow = AuthorizationCodeGrant(
        doc['client_id'],
        doc['scopes'],
        doc['client_secret'],
        doc['redirect_url']
    )
    return auth_flow

def import_oauth2_credentials(filename=STORAGE_FILENAME):

    with open(filename, 'r') as storage_file:
        storage = yaml.load(storage_file)

    # depending on OAuth 2.0 grant_type, these values may not exist
    client_secret = storage.get('client_secret')
    redirect_url = storage.get('redirect_url')
    refresh_token = storage.get('refresh_token')

    credentials = {
        'access_token': storage['access_token'],
        'client_id': storage['client_id'],
        'client_secret': client_secret,
        'expires_in_seconds': storage['expires_in_seconds'],
        'grant_type': storage['grant_type'],
        'redirect_url': redirect_url,
        'refresh_token': refresh_token,
        'scopes': storage['scopes'],
    }

    return credentials


def authorization_code_grant(storage_filename):
    auth_flow = import_app_credentials()
    auth_url = auth_flow.get_authorization_url()

    login_message = 'Login and grant access by going to:\n{}\n'
    login_message = login_message.format(auth_url)
    print(login_message)

    try:
        result = raw_input('Copy paste').strip()
    except (ClientError, ServerError) as error:
        fail_print(error)

    session = auth_flow.get_session(result)
    client = UberRidesClient(session, sandbox_mode=True)
    credentials = session.oauth2credential

    response = client.get_user_profile()
    profile = response.json

    first_name = profile.get('first_name')
    last_name = profile.get('last_name')
    email = profile.get('email')

    print first_name, " ", last_name, " ",email

def create_uber_client(credentials):
    """Create an UberRidesClient from OAuth 2.0 credentials.
    Parameters
        credentials (dict)
            Dictionary of OAuth 2.0 credentials.
    Returns
        (UberRidesClient)
            An authorized UberRidesClient to access API resources.
    """
    oauth2credential = OAuth2Credential(
        client_id=credentials.get('client_id'),
        access_token=credentials.get('access_token'),
        expires_in_seconds=credentials.get('expires_in_seconds'),
        scopes=credentials.get('scopes'),
        grant_type=credentials.get('grant_type'),
        redirect_url=credentials.get('redirect_url'),
        client_secret=credentials.get('client_secret'),
        refresh_token=credentials.get('refresh_token'),
    )
    session = Session(oauth2credential=oauth2credential)
    return UberRidesClient(session, sandbox_mode=True)

def getStartLoc(db,deviceID):
    iot = IoT(db)
    key = iot.getAlpha(deviceID)
    add = iot.getAdd(key)
    print add
    start_geocode = gmaps.geocode(add)
    slat = start_geocode[0]['geometry']['location']['lat']
    slong = start_geocode[0]['geometry']['location']['lng']
    return slat , slong, key



def getEndLoc(endAdd):
    end_geocode = gmaps.geocode(endAdd)
    elat = end_geocode[0]['geometry']['location']['lat']
    elong = end_geocode[0]['geometry']['location']['lng']
    return elat , elong



credentials = import_oauth2_credentials()
client = create_uber_client(credentials)
db = firebase.database()
iot = IoT(db)

#voice input
add = 'aissms college of engineering'
seats = 2

slat, slng, user_key = getStartLoc(db,deviceID)
elat, elng = getEndLoc(add)


response = client.get_products(slat, slng)
products = response.json.get('products')

product_id = products[0].get('product_id')

print products[0]['short_description']

# Get upfront fare for product with start/end location
estimate = client.estimate_ride(
    product_id=product_id,
    start_latitude=slat,
    start_longitude=slng,
    end_latitude=elat,
    end_longitude=elng,
    seat_count=seats
)

fare = estimate.json.get('fare')
print fare['value'],fare['currency_code']

#Request ride with upfront fare for product with start/end location
response = client.request_ride(
    product_id=product_id,
    start_latitude=slat,
    start_longitude=slng,
    end_latitude=elat,
    end_longitude=elng,
    seat_count=seats,
    fare_id=fare['fare_id']
)

request = response.json
request_id = request.get('request_id')
print "Request ID:", request_id
iot.setRideKey(request_id,user_key)

#Request ride details from request_id
response = client.get_ride_details(request_id)
ride = response.json
print ride
print "Ride requested successfully"

response = client.get_pickup_time_estimates(
    slat,
    slng,
    product_id = product_id
)
print response.json
# Cancel a ride
#response = client.cancel_ride(request_id)
#ride = response.json
#print "Ride Cancelled"
