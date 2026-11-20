
from fastapi import FastAPI
from pydantic import BaseModel
from search_service import search_google
from gemini_service import summarize_results
app = FastAPI()

class ResearchRequest(BaseModel):
    topic:str

@app.post("/research")
async def research_topic(data: ResearchRequest):
    results = await search_google(data.topic)
    summary = await summarize_results(data.topic, results)

    # Step 3: Return the final response
    return {
        "topic": data.topic,
        "search_results": results,
        "summary": summary
    }


@app.get("/")
async def home():
    return {"message": "AI Research Assistant is running!"}



