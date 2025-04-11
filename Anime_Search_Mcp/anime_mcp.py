import requests
import json
import logging
import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize MCP Server
mcp = FastMCP("anime_db")

# API Configuration
API_BASE = "https://anime-db.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
    "x-rapidapi-host": "anime-db.p.rapidapi.com"
}

def fetch_anime_genres() -> dict:
    """Fetch available anime genres."""
    url = f"{API_BASE}/genre"
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch genres: {e}")
        return {"status": "error", "message": str(e)}

def fetch_anime_list(page: int, size: int, genres: str) -> dict:
    """Fetch a list of anime based on genres and pagination.

    Args:
        page: Page number (1, 2, etc.).
        size: Number of results per page.
        genres: Comma-separated list of genres (e.g., "Fantasy,Drama").
    """
    url = f"{API_BASE}/anime"
    params = {"page": str(page), "size": str(size), "genres": genres}

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch anime list: {e}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def get_anime_genres() -> str:
    """Retrieve all available anime genres."""
    data = fetch_anime_genres()
    return json.dumps(data, indent=2)

@mcp.tool()
def get_anime_list(page: int, size: int, genres: str) -> str:
    """Retrieve a list of anime based on genres.

    Args:
        page: Page number (e.g., 1).
        size: Number of results per page (e.g., 50).
        genres: Comma-separated genres (e.g., "Fantasy,Drama").
    """
    data = fetch_anime_list(page, size, genres)
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
