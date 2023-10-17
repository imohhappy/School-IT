import datetime as dt
import requests

#BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=5a6a3c01aa872bfebb3e7d3f663ede3e"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
api_keys="5a6a3c01aa872bfebb3e7d3f663ede3e"

CITY = "Uyo"

url = BASE_URL + "appid=" + api_keys + "&q=" + CITY

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

response = requests.get(url).json()

temp_kelvin = response["main"]["temp"]
temp_celsius,temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.today()
sunset_time = dt.datetime.today()

print(f'Temperature in {CITY}: {temp_celsius: .2f}c or {temp_fahrenheit: .2f}f')
print(f'Temperature in {CITY} feels like: {feels_like_celsius: .2f}c or {feels_like_fahrenheit: .2f}f')
print(f'Humidity {CITY}: {humidity}%')
print(f'Description {CITY}: {description}')
print(f'Wine Speed {CITY}: {wind_speed}km/h')
print(f'Sun rises in {CITY} at {sunrise_time} local time')
print(f'Sun set in {CITY} at {sunset_time} local time')
