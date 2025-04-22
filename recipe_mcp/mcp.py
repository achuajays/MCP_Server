import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load env vars
load_dotenv()
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in the .env file")

mcp = FastMCP("dynamic_recipe_finder")

@mcp.tool()
def get_recipes(tags: str = "vegetarian,dessert", number: int = 1) -> dict:
    """
    Get random recipes by tags and number.
    Example: tags="vegetarian,dessert", number=2
    """
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
    querystring = {"tags": tags, "number": str(number)}
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

if __name__ == "__main__":
    mcp.run()
