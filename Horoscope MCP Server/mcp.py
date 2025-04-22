# 1. Horoscope MCP Server
import os
import json
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in .env")

mcp = FastMCP("daily_horoscope")

@mcp.tool()
def get_daily_horoscope(zodiac: str = "aquarius") -> str:
    url = "https://astropredict-daily-horoscopes-lucky-insights.p.rapidapi.com/horoscope"
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "astropredict-daily-horoscopes-lucky-insights.p.rapidapi.com"
    }
    params = {"lang": "en", "zodiac": zodiac, "type": "daily"}
    response = requests.get(url, headers=headers, params=params)
    return json.dumps(response.json(), indent=2)