import requests
from semantic_kernel.functions import kernel_function

class WeatherPlugin:

    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    @kernel_function(description="Gets the weather for a location in future.")
    async def get_weather_forecast(self, latitude: float, longitude: float, days: int = 1) -> dict:
        url = f"{self.base_url}?latitude={latitude}&longitude={longitude}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,weather_code,cloud_cover,wind_speed_10m,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&forecast_days={days}"
        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    
    @kernel_function(description="Gets the weather for a location in the past.")
    async def get_past_weather(self, latitude: float, longitude: float, days: int = 1) -> dict:
        url = f"{self.base_url}?latitude={latitude}&longitude={longitude}&past=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,showers,snowfall,weather_code,cloud_cover,wind_speed_10m,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&past_days={days}"
        response = requests.get(url)
        response.raise_for_status()

        return response.json()