import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in .env")

mcp = FastMCP("watch_searcher")


@mcp.tool()
def search_watches_by_name(searchTerm: str, page: int = 1, limit: int = 20) -> dict:
    """
    Search for watches by name using the Watch Database API.

    Args:
        searchTerm: The name or keyword of the watch to search.
        page: The page of results to fetch.
        limit: The number of results per page.

    Returns:
        JSON response containing the watch search results.
    """
    url = "https://watch-database1.p.rapidapi.com/search-watches-by-name"
    payload = {
        "searchTerm": searchTerm,
        "page": str(page),
        "limit": str(limit)
    }
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "watch-database1.p.rapidapi.com",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response.json()


if __name__ == "__main__":
    mcp.run()
