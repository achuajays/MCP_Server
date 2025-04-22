import requests
import json
import logging
from mcp.server.fastmcp import FastMCP

# Initialize MCP Server
mcp = FastMCP("cricbuzz_player_news")

# API Configuration
API_BASE = "https://cricbuzz-cricket.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-key": "",
    "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

def search_player(player_name: str) -> dict:
    """Search for a player by name and return player details."""
    url = f"{API_BASE}/stats/v1/player/search"
    params = {"plrN": player_name}

    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("player", [])[0] if "player" in data and data["player"] else None
    except Exception as e:
        logging.error(f"Failed to search player: {e}")
        return None

def fetch_player_news(player_id: str) -> dict:
    """Fetch career news for a given player ID."""
    url = f"{API_BASE}/news/v1/player/{player_id}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error(f"Failed to fetch player news: {e}")
        return {"status": "error", "message": str(e)}

@mcp.tool()
def get_player_news(player_name: str) -> str:
    """Retrieve career news for a given cricket player.

    Args:
        player_name: The name of the cricket player.
    """
    player = search_player(player_name)
    if not player:
        return json.dumps({"status": "error", "message": "Player not found"}, indent=2)

    player_id = player["id"]
    news_data = fetch_player_news(player_id)

    return json.dumps({
        "player": player,
        "news": news_data
    }, indent=2)

if __name__ == "__main__":
    mcp.run(transport="stdio")
