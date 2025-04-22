from mcp.server.fastmcp import FastMCP
import os
import requests
from dotenv import load_dotenv

load_dotenv()
mcp = FastMCP("dev_jokes")

RAPID_API_KEY = os.getenv("RAPID_API_KEY")

@mcp.tool()
def get_joke(category: str = "all", subcategory: str = "javascript") -> dict:
    url = "https://quotes-api12.p.rapidapi.com/dev-jokes"
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "quotes-api12.p.rapidapi.com"
    }
    params = {"category": category, "subcategory": subcategory}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

if __name__ == "__main__":
    mcp.run()
