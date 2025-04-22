import os
import json
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in the environment variables")

mcp = FastMCP("youtube_mp3_downloader")

API_URL = "https://yt-search-and-download-mp3.p.rapidapi.com/mp3"
API_HOST = "yt-search-and-download-mp3.p.rapidapi.com"


def fetch_mp3_info(youtube_url: str) -> dict:
    """Fetch MP3 download info from YouTube link."""
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": API_HOST
    }
    params = {"url": youtube_url}

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def get_mp3_download_link(youtube_url: str) -> str:
    """Get download info for a YouTube video in MP3 format."""
    data = fetch_mp3_info(youtube_url)
    return json.dumps(data, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
