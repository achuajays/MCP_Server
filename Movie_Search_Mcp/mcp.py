import requests
import json
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables from the .env file
load_dotenv()

# Retrieve the RAPID_API_KEY from the environment variables
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in the environment variables")

# Initialize the MCP server
mcp = FastMCP("movie_finder")

# API Configuration
API_URL = "https://imdb236.p.rapidapi.com/imdb/most-popular-tv"
HEADERS = {
    "x-rapidapi-key": RAPID_API_KEY,
    "x-rapidapi-host": "imdb236.p.rapidapi.com"
}

def fetch_most_popular_tv() -> dict:
    """Fetch the most popular TV shows from IMDb."""
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

@mcp.tool()
def get_popular_tv_shows() -> str:
    """Retrieve the most popular TV shows from IMDb."""
    data = fetch_most_popular_tv()
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
