# weather_api.py
# ============================================================
# Weather API — Tutorial
# Fetch real-time weather data using Open-Meteo (no API key needed)
# Docs: https://open-meteo.com
# ============================================================

import requests

# ---- 1. SET LOCATION ----
# Latitude and longitude for London
LATITUDE = 51.5074
LONGITUDE = -0.1278
CITY = "London"

BASE_URL = "https://api.open-meteo.com/v1/forecast"


# ---- 2. BUILD THE REQUEST ----

params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "current_weather": True,
    "hourly": "temperature_2m,precipitation,windspeed_10m",
    "timezone": "Europe/London"
}

response = requests.get(BASE_URL, params=params)
data = response.json()


# ---- 3. CURRENT WEATHER ----

current = data["current_weather"]

print(f"=== Current Weather in {CITY} ===")
print(f"Temperature:  {current['temperature']}°C")
print(f"Wind Speed:   {current['windspeed']} km/h")
print(f"Wind Direction: {current['winddirection']}°")

# Weather code meaning
weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    80: "Rain showers",
}
code = current["weathercode"]
condition = weather_codes.get(code, f"Code {code}")
print(f"Condition:    {condition}")


# ---- 4. HOURLY FORECAST (next 5 hours) ----

hourly = data["hourly"]

print(f"\n=== Hourly Forecast ===")
for i in range(5):
    time = hourly["time"][i]
    temp = hourly["temperature_2m"][i]
    rain = hourly["precipitation"][i]
    wind = hourly["windspeed_10m"][i]
    print(f"{time}  |  {temp}°C  |  Rain: {rain}mm  |  Wind: {wind} km/h")


# ---- 5. TRY ANOTHER CITY ----
# Change latitude/longitude to get weather for any city
# Dublin:    53.3498, -6.2603
# New York:  40.7128, -74.0060
# Tokyo:     35.6762, 139.6503