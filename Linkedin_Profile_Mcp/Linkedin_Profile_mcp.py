import requests
import json
import os
import logging
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# Initialize MCP Server
mcp = FastMCP("linkedin_profile_fetcher")

# API Configuration
API_URL = "https://linkedin-data-api.p.rapidapi.com/get-profile-data-by-url"
HEADERS = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}

def fetch_linkedin_profile(url: str) -> dict:
    """Fetch LinkedIn profile data for the given profile URL."""
    params = {"url": url}

    try:
        response = requests.get(API_URL, headers=HEADERS, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch LinkedIn profile: {e}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def get_linkedin_profile(url: str) -> str:
    """Retrieve LinkedIn profile data based on a profile URL.

    Args:
        url: The LinkedIn profile URL.
    """
    data = fetch_linkedin_profile(url)
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
