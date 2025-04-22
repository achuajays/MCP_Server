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
mcp = FastMCP("netflix_series_details")

# API Configuration for Netflix API
API_URL = "https://netflix133.p.rapidapi.com/content"
HEADERS = {
    "x-rapidapi-key": RAPID_API_KEY,
    "x-rapidapi-host": "netflix133.p.rapidapi.com"
}


def fetch_series_details(content_id: str) -> dict:
    """Fetch the details of a Netflix series based on the content ID."""
    querystring = {"contentId": content_id}

    try:
        response = requests.get(API_URL, headers=HEADERS, params=querystring, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def get_series_details(content_id: str) -> str:
    """Retrieve Netflix series details using a content ID."""
    data = fetch_series_details(content_id)
    return json.dumps(data, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
