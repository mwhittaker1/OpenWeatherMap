import requests


root_url = "https://api.openweathermap.org/data/3.0/onecall/overview?"
#city_name = input("What city would you like weather from?")
api_key = "be075386dbc2d586f564edbca78d530a"
lon= -74.949203
lat= 39.857819
url = f"{root_url}lat={lat}&lon={lon}&appid={api_key}"
r = requests.get(url)

#print(r.json())

data = r.json()

overview = data['weather_overview']

print(f"Weather Overview: {overview}")

"""if data['cod'] == 200:
    temp = data['current.temp']

    pressure = data['current.pressure']

    humidity = data['current.humidity']

    wind = data['current.wind_speed']

    print(f"Temprature: {temp}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Wind speed: {wind}")

#error response
else:
    print(f"Sorry, something went wrong.")

cod = data['main']['cod']

temp = data['current']['temp']

pressure = data['current.pressure']

humidity = data['current.humidity']

wind = data['current.wind_speed']

print(f"Erro Code: {cod}")
print(f"Temprature: {temp}")
print(f"Humidity: {humidity}")
print(f"Pressure: {pressure}")
#rint(f"Wind speed: {wind}")"""

