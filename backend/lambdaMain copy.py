import requests
import datetime
import pytz
import os

API_KEY = os.environ("API_KEY")
root_url = "https://api.openweathermap.org/data/3.0/onecall?"
c = "current"

#gets location from state/zipcode
def get_location(state, zipcode):
   print("Getting location...")
   location_data = requests.get(
       f"https://api.openweathermap.org/geo/1.0/zip?zip={zipcode},{state}&appid={API_KEY}"
   ).json()
   lat = location_data["lat"]
   lon = location_data["lon"]
   return lat, lon


#pulls data from url
def get_weather(zip: str, lat, lon):
   print("Getting weather...")
   exclude = "hourly,daily,minutely"
   url = f"{root_url}lat={lat}&lon={lon}&exclude={exclude}&appid={API_KEY}".strip(
   )
   r = requests.get(url)
   data = r.json()
   #print(f"Data fetched! {data}")
   return data


#get time from data
def weather_time(weather_info):
   print("Getting time...")
   time = weather_info[c]['dt']
   utc_time = datetime.datetime.fromtimestamp(time)
   est = pytz.timezone('US/Eastern')
   time = utc_time.astimezone(est)
   return weather_info, time


#get temp from data
def weather_temp(weather_info):
   print("Getting temp...")
   temp = weather_info[c]['temp']
   temp = round((temp - 273.15) * 1.8 + 32)
   return weather_info, temp


#get humidity from data
def weather_humidity(weather_info):
   print("Getting humidity...")
   humidity = weather_info[c]['humidity']
   return weather_info, humidity


#get cloud percent from data
def weather_cloudPercent(weather_info):
   print("Getting cloud percent...")
   cloudPercent = weather_info[c]['clouds']
   return weather_info, cloudPercent


#format time, temp, humidity, and cloud percent into strings
def format_weather(weather_info, time, temp, humidity, cloudPercent):
   print("Formatting weather...")
   str_time = "time: " + str(time) + " | "
   str_temp = "temp: " + str(temp) + " | "
   str_humidity = "humidity: " + str(humidity) + " | "
   str_cloudPercent = "Cloud Cover Percent: " + str(cloudPercent) + " | "
   return str_time, str_temp, str_humidity, str_cloudPercent


def hardcode_location():
   lon = -74.949203
   lat = 39.857819
   return lon, lat


def build_message(str_time, str_temp, str_humidity, str_cloudPercent):
   print("Building message...")
   b = "\n"
   welcome = f"{b}{b}Welcome here's the weather for Voorhees, NJ!{b}"
   message = welcome + b + str_time + b + b + str_temp + b + b + str_humidity + b + b + str_cloudPercent
   return message


#main function to run all functions

def lambda_handler(event, context):
   print("Running main...")
   
   zip_code = None
   if event.get("queryStringParameters") and "zip" in event["queryStringParameters"]:
      zip_code = event["queryStringParameters"]["zip"]

   
   #lat, lon = get_location("NJ", "08043")
   lon, lat = hardcode_location()
   weather_info = get_weather(context, lat, lon)
   weather_info, time = weather_time(weather_info)
   weather_info, temp = weather_temp(weather_info)
   weather_info, humidity = weather_humidity(weather_info)
   weather_info, cloudPercent = weather_cloudPercent(weather_info)
   str_time, str_temp, str_humidity, str_cloudPercent = format_weather(
       weather_info, time, temp, humidity, cloudPercent)
   message = build_message(str_time, str_temp, str_humidity, str_cloudPercent)
   print("Message built!")
   print(message)
   return {
      "statusCode": 200,
      "headers":{
         "Content-Type": "text/plain"
      },
      "body": message
   }