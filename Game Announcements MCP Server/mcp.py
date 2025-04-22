from mcp.server.fastmcp import FastMCP
import os
import requests
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("game_announcements")

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

@mcp.tool()
def get_game_news(limit: int = 10, offset: int = 0) -> dict:
    url = "https://games-details.p.rapidapi.com/news/announcements/3240220"
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    params = {"limit": str(limit), "offset": str(offset)}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    mcp.run()
