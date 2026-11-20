import os     #Reads environment variables
from dotenv import load_dotenv #Loads API keys from your .env file
#from serpapi import GoogleSearch #Communicates with SerpAPI's Google Search API

import httpx


load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
if not SERPAPI_KEY:
    raise ValueError("SERPAPI_API_KEY is missing from .env")

async def search_google(topic: str,limit: int = 10):
    search_query = f'"{topic}"'

    params = {
        "engine": "google",
        "q": search_query,
        "api_key": SERPAPI_KEY,
        "google_domain": "google.co.in",
        "gl": "in",
        "hl": "en",
        "num": 10,
        "nfpr": 1
    }

    async with httpx.AsyncClient(timeout=60.0) as client: #Creates an asynchronous HTTP client
        response = await client.get(  # await Waits for an asynchronous operation without blocking the event loop
            "https://serpapi.com/search.json",
            params=params
        )

        response.raise_for_status() #Check whether the HTTP request was successful. If the server returned an HTTP error status code, raise an exception.

        results = response.json() #Converts the JSON response into a Python object (usually a dictionary).

    organic_results = results.get("organic_results",[])
    filtered_results = []
    for item in organic_results:
        data = {
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        }
        filtered_results.append(data)
    return filtered_results[:limit]  # it returns only 10 rows of data
