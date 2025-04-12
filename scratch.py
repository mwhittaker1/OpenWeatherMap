import requests
import datetime
import pytz
import os

API_KEY = "be075386dbc2d586f564edbca78d530a"
root_url = "https://api.openweathermap.org/data/3.0/onecall?"
c = "current"
lon = -74.949203
lat = 39.857819


#get time from data
def weather_time(weather_info):
   print("Getting time...")
   time = weather_info[c]['dt']
   utc_time = datetime.datetime.fromtimestamp(time)
   est = pytz.timezone('US/Eastern')
   time = utc_time.astimezone(est)
   stime = str(time)
   year = stime[:4]
   date = stime[5:10]
   hourmin = stime[11:16]
   return time, date, year, hourmin

def get_weather(lat, lon):
   print("Getting weather...")
   exclude = "hourly,daily,minutely"
   url = f"{root_url}lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}".strip(
   )
   r = requests.get(url)
   data = r.json()
   #print(f"Data fetched! {data}")
   return data


data = get_weather(lat,lon)
time, date, year, hourmin = weather_time(data)
print(f"time in EST: {time} year = {year} date = {date}, and time = {hourmin} data = \nFormatted to: It is currently {hourmin} on {date}-{year}")