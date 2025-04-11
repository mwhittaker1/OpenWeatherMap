from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import datetime
import pytz
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

root_url = "https://api.openweathermap.org/data/3.0/onecall?"
#city_name = input("What city would you like weather from?")
API_KEY = os.getenv("API_KEY")
#API_KEY = "be075386dbc2d586f564edbca78d530a"
lon= -74.949203
lat= 39.857819
exclude= "hourly,daily,minutely"
url = f"{root_url}lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}"
r = requests.get(url)
c = "current"

#pulls data from url and prints
r = requests.get(url)
data = r.json()
print(f"Data fetched!")

#sorts data into variables

time = data[c]['dt']
utc_time = datetime.datetime.fromtimestamp(time)
est = pytz.timezone('US/Eastern')
time = utc_time.astimezone(est)
print(f"date \ time: {time}")

temp = data[c]['temp']
temp = round((temp - 273.15)*1.8+32)
print(f"temp: {temp}")

humidity = data[c]['humidity']
print(f"humidity: {humidity}")

cloudPercent = data[c]['clouds']
print(f"cloud %: {cloudPercent}")

str_time = "time: " + str(time) + " | "
str_temp = "temp: " + str(temp) + " | "
str_humidity = "humidity: " + str(humidity) + " | "
str_cloudPercent = "Cloud Cover Percent: " + str(cloudPercent) + " | "

b = "\n"

welcome = "Welcome Emily! You wanted to know the weather right?"
message = str_time +b+b+ str_temp +b +b + str_humidity +b+b+ str_cloudPercent
print(f"Trying to combine into one string!: \n\n{message}")

@app.get("/", response_class=HTMLResponse)
def read_root():
   return f"{welcome}{b}{b}{b}{message}"
