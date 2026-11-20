import os
from dotenv import load_dotenv
from tavily import AsyncTavilyClient
load_dotenv()

Tavily_API_KEY = os.getenv("TAVILY_API_KEY")
if not Tavily_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing from .env")
client = AsyncTavilyClient(api_key=Tavily_API_KEY)

async def search_tavily(topic: str, limit: int = 10):

    response = await client.search(
        query=topic,
        search_depth="basic",
        max_results=limit
    )

    results = response.get("results", [])

    filtered_results = []

    for item in results:
        data = {
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content"),
            "score": item.get("score")
        }

        filtered_results.append(data)

    return filtered_results
