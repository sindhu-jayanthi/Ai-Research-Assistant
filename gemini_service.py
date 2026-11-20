import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors
load_dotenv()

client = genai.Client(  #creates a Gemini client to communicate with Google's API.
    api_key=os.getenv("GEMINI_API_KEY")
)

async def summarize_results(topic: str, search_results: list):

    prompt = f"""
    You are an AI research assistant.

    Research Topic: {topic}

    Analyse the following Google search results:

    {search_results}

    Provide:
    1. A concise summary.
    2. Five key findings.
    3. Important source links.
    4. Any conflicting or insufficient information.
    """
    try:
      response = await client.aio.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
      )

      return response.text
    except errors.ServerError as error:
       print("Gemini server error:", error)
       return "Gemini is temporarily unavailable. Please try again later."
