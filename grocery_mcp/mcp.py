import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in .env")

mcp = FastMCP("grocery_price_finder")


@mcp.tool()
def get_grocery_prices(keyword: str, perPage: int = 10, page: int = 1) -> dict:
    """
    Search real-time grocery pricing data.

    Args:
        keyword: The grocery item to search (e.g., "sweet potato").
        perPage: Results per page.
        page: Page number.

    Returns:
        JSON response with grocery pricing data.
    """
    url = "https://grocery-pricing-api.p.rapidapi.com/searchGrocery"
    querystring = {
        "keyword": keyword,
        "perPage": str(perPage),
        "page": str(page)
    }
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "grocery-pricing-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


if __name__ == "__main__":
    mcp.run()