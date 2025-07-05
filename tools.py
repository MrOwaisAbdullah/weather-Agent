from agents import function_tool
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

@function_tool
def get_weather(location: str) -> str:
    """
    Fetches the current weather for a given location using API.

    Args:
        location (str): The name of the location to get the weather for.
    """
    response = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}"
    )
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    return "Error fetching weather data."