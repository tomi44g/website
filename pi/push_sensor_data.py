#!/usr/bin/python3


import sys
import Adafruit_DHT
from firebase import Firebase
from datetime import datetime

sensor = Adafruit_DHT.AM2302
pin = 2

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


# Update data in Firebase
config = {
  "apiKey": "AIzaSyAnU0SI-NcBOYwuf8TQBpMcdUgtd8zrpA4",
  "authDomain": "tbc",
  "databaseURL": "https://deep-scoring.firebaseio.com",
  "storageBucket": "tbc.appspot.com"
}

firebase = Firebase(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("pi@deepscoring.com", "Banbury44;Password")
token = user['idToken']

db = firebase.database()
data = {"temp": round(temperature, 1), 
        "rh":round(humidity, 1), 
        "time": datetime.today().isoformat()}
db.child("sensors").child("latest").update(data, token)
db.child("sensors").child("data").push(data, token)


