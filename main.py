
from fastapi import FastAPI
from pydantic import BaseModel
from search_service import search_google
from gemini_service import summarize_results
from tavily_service import search_tavily
import asyncio
app = FastAPI()

class ResearchRequest(BaseModel):
    topic:str

@app.post("/research")  #serp+gemini integration
async def research_topic(data: ResearchRequest):
    results = await search_google(data.topic)
    summary = await summarize_results(data.topic, results)

    # Step 3: Return the final response
    return {
        "topic": data.topic,
        "search_results": results,
        "summary": summary
    }


@app.post("/compare-search") #to get both search results
async def compare_search(data: ResearchRequest):

    google_results, tavily_results = await asyncio.gather( #both search can run simultaniously and reduce time
        search_google(data.topic),
        search_tavily(data.topic)
    )

    return {
        "topic": data.topic,
        "serpapi_results": google_results,
        "tavily_results": tavily_results
    }

@app.post("/research-combined") #serp and Tavily api's
async def research_combined(data: ResearchRequest):

    google_results, tavily_results = await asyncio.gather(
        search_google(data.topic),
        search_tavily(data.topic)
    )

    combined_results = []

    for item in google_results:
        combined_results.append({
            "source": "SerpAPI",
            "title": item.get("title"),
            "link": item.get("link"),
            "content": item.get("snippet")
        })

    for item in tavily_results:
        combined_results.append({
            "source": "Tavily",
            "title": item.get("title"),
            "link": item.get("url"),
            "content": item.get("content"),
            "score": item.get("score")
        })

    summary = await summarize_results(
        data.topic,
        combined_results
    )

    return {
        "topic": data.topic,
        "search_results": combined_results,
        "summary": summary
    }






@app.get("/")
async def home():
    return {"message": "AI Research Assistant is running!"}



