from mcp.server.fastmcp import FastMCP
import os
import requests
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("instagram_viewer")

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

@mcp.tool()
def view_profile(profile: str) -> dict:
    url = "https://instagram-viewer.p.rapidapi.com/instagram-viewer"
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "instagram-viewer.p.rapidapi.com"
    }
    params = {"profile": profile}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    mcp.run()
