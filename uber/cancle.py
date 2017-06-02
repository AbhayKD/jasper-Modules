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
            print key
            return key
        except:
            print "Try Again"
            return
    def getKey(self,key):
        try:
            data = self.db.child('Users').child(key).child('Uber').get()
            add = data.val()
            return add
        except:
            print "Error, try again"
            return

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

credentials = import_oauth2_credentials()
client = create_uber_client(credentials)
db = firebase.database()
iot = IoT(db)
userID = iot.getAlpha(deviceID)
request_id = iot.getKey(userID)['id']
print request_id

# Cancel a ride
response = client.cancel_ride(request_id)
ride = response.json
print "Ride Cancelled"
