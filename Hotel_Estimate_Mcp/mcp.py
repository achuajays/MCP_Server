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
mcp = FastMCP("hotel_estimate_service")

# API Configuration for Hotel Estimate API
API_URL = "https://carbonsutra1.p.rapidapi.com/hotel_estimate"
HEADERS = {
    "x-rapidapi-key": RAPID_API_KEY,
    "x-rapidapi-host": "carbonsutra1.p.rapidapi.com",
    "Content-Type": "application/x-www-form-urlencoded"
}


def fetch_hotel_estimate() -> dict:
    """Fetch hotel estimate using Carbonsutra API."""
    payload = {}

    try:
        response = requests.post(API_URL, data=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}


@mcp.tool()
def get_hotel_estimate() -> str:
    """Get the hotel cost estimate."""
    data = fetch_hotel_estimate()
    return json.dumps(data, indent=2)


if __name__ == "__main__":
    mcp.run(transport="stdio")
