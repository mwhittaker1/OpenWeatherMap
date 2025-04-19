from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
import datetime
import pytz
from dotenv import load_dotenv
import os
import uvicorn
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
root_url = "https://api.openweathermap.org/data/3.0/onecall?"
c = "current"
zip_code = "08043"
country_code = "US"
#gets location from state/zipcode
def get_location(zipcode):
   print("Getting location...")
   location_data = requests.get(
       f"http://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{country_code}&appid={API_KEY}"
   ).json()
   lat = location_data["lat"]
   lon = location_data["lon"]
   return lat, lon, location_data

lat, lon, data = get_location(zip_code)
print(f"lat :{lat}, long:{lon}")
print(f"full package: {data}")