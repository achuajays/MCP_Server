import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in .env")

mcp = FastMCP("weather_fetcher")


@mcp.tool()
def get_weather(location: str) -> dict:
    """
    Fetches the weather data for the provided location using the Yahoo Weather API.

    Args:
        location: The location for which weather details are required.

    Returns:
        JSON response containing weather data.
    """
    url = "https://yahoo-weather5.p.rapidapi.com/weather"
    querystring = {"location": location, "format": "json", "u": "f"}
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


if __name__ == "__main__":
    mcp.run()
