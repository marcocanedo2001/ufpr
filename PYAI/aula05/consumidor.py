import requests

cidade = "Curitiba"

geo_url = "https://geocoding-api.open-meteo.com/v1/search"

geo_params = {"name": cidade, "count": 1}
geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()
lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]

print(f"Latitude: {lat}, Longitude: {lon}")

weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": True,
}
weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()
print(
    f"Temperatura atual em {cidade}: {weather_data['current_weather']['temperature']}°C"
)
