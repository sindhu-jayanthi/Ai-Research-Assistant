# AI Research Assistant 🔍🤖

An AI-powered research assistant built using **Python, FastAPI, SerpAPI, Tavily and Google Gemini**.

The application retrieves information from multiple web search providers, combines the results and uses a Large Language Model (LLM) to generate research summaries with supporting source links.

The project explores multi-source information retrieval, asynchronous API integration and AI-powered content summarisation.

## 🚀 Project Overview

The AI Research Assistant allows users to enter a research topic and retrieve relevant information from multiple search providers.

It integrates:

- **SerpAPI** – Retrieves structured Google Search results.
- **Tavily API** – Retrieves AI-focused web search results and relevant content.
- **Google Gemini** – Analyses retrieved information and generates research summaries.
- **FastAPI** – Provides REST API endpoints for the application.

The objective is to compare different search providers and combine their information to support more comprehensive AI-generated research.

## 🏗️ Architecture

```text
                 User
                   |
                   v
             FastAPI Application
                   |
          Research Topic Input
                   |
          ---------------------
          |                   |
          v                   v
       SerpAPI              Tavily
          |                   |
    Google Search       AI Web Search
          |                   |
          v                   v
      Search Results     Search Results
          |                   |
          ---------+----------
                   |
                   v
          Combine Search Results
                   |
                   v
             Google Gemini
                   |
                   v
          AI-Generated Summary
                   |
                   v
        Research Report with Links
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| HTTPX | Asynchronous HTTP requests |
| SerpAPI | Google Search integration |
| Tavily | AI-focused web search |
| Google Gemini | AI summarisation |
| Pydantic | Request data validation |
| Python-dotenv | Environment variable management |
| Uvicorn | ASGI application server |

## 🔗 API Integrations

### 1. SerpAPI Integration

SerpAPI is integrated to retrieve structured Google Search results.

**Implementation:**
- Sends the user's research topic to the Google Search API.
- Retrieves organic search results.
- Extracts titles, URLs and snippets.
- Returns structured results for further processing.

**Fields extracted:**
- `title`
- `link`
- `snippet`

### 2. Tavily API Integration

Tavily is integrated as a second search provider to retrieve relevant web research content.

**Implementation:**
- Uses the asynchronous Tavily Python client.
- Accepts the user's research topic as a query.
- Retrieves relevant search results.
- Extracts titles, URLs, content and relevance scores.

**Fields extracted:**
- `title`
- `url`
- `content`
- `score`

### 3. Google Gemini Integration

Google Gemini is used to analyse the retrieved search information and generate an AI-powered research summary.

The summarisation process includes:
- Concise research summaries.
- Key findings.
- Important source links.
- Conflicting or insufficient information.

## ⚡ Asynchronous Processing

The application uses Python's asynchronous programming capabilities.

`async` and `await` are used for asynchronous API operations.

`asyncio.gather()` executes the independent SerpAPI and Tavily search requests concurrently.

This helps reduce the total search execution time compared with performing the requests sequentially.

## 📂 Project Structure

```text
AI_Research_Assistant/
│
├── main.py
├── search_service.py
├── tavily_service.py
├── gemini_service.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

**File descriptions:**

| File | Description |
|---|---|
| `main.py` | FastAPI application and API endpoints |
| `search_service.py` | SerpAPI Google Search integration |
| `tavily_service.py` | Tavily search integration |
| `gemini_service.py` | Gemini AI summarisation |
| `requirements.txt` | Python project dependencies |
| `.env` | API keys and environment variables |
| `.gitignore` | Files excluded from Git tracking |

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- SerpAPI account and API key
- Tavily account and API key
- Google Gemini API key

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_Research_Assistant.git
```

Navigate to the project directory:

```bash
cd AI_Research_Assistant
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install the main packages:

```bash
pip install fastapi uvicorn httpx python-dotenv google-genai tavily-python
```

### Step 4: Configure environment variables

Create a `.env` file in the project root.

Add the following variables:

```env
SERPAPI_API_KEY=your_serpapi_api_key
TAVILY_API_KEY=your_tavily_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholders with your actual API keys.

**Security note:** Never upload your `.env` file or expose API keys in your source code or GitHub repository.

### Step 5: Run the application

```bash
uvicorn main:app --reload
```

The application will run locally at:

```text
http://127.0.0.1:8000
```

Access the interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## 📡 API Endpoints

### 1. Home

**Method:** GET

**Endpoint:** `/`

Checks whether the application is running.

### 2. Research

**Method:** POST

**Endpoint:** `/research`

Performs a Google search using SerpAPI and sends the retrieved results to Gemini for summarisation.

Example request:

```json
{
  "topic": "Artificial Intelligence in healthcare"
}
```

### 3. Compare Search

**Method:** POST

**Endpoint:** `/compare-search`

Runs SerpAPI and Tavily searches concurrently and returns their results separately for comparison.

Example request:

```json
{
  "topic": "Artificial Intelligence in healthcare"
}
```

### 4. Combined Research

**Method:** POST

**Endpoint:** `/research-combined`

Runs both search integrations, combines the retrieved information into a common structure and sends it to Gemini for AI-generated summarisation.

Example request:

```json
{
  "topic": "Indian artificial intelligence market growth"
}
```

The response includes:

- Research topic.
- Combined search results.
- Search provider information.
- Gemini-generated research summary.

## 🎯 Key Features

- Multiple web search integrations.
- Concurrent API requests.
- Asynchronous processing using Python.
- Structured search result extraction.
- Search provider comparison.
- AI-powered research summarisation.
- Source links for further verification.
- REST API development using FastAPI.
- Environment-based API key management.

## 🔮 Future Enhancements

The following features are planned for future development:

- Duplicate URL detection and removal.
- Search relevance comparison and evaluation.
- Improved source credibility assessment.
- Retrieval-Augmented Generation (RAG).
- Document upload and question answering.
- Vector database integration.
- AI agent and tool-calling capabilities.
- Research report export to PDF.
- Frontend dashboard.
- Cloud deployment.

## 📚 Learning Outcomes

This project provides hands-on experience with:

- Integrating multiple third-party APIs.
- Building asynchronous Python applications.
- Developing REST APIs using FastAPI.
- Handling JSON responses and transforming data.
- Integrating Large Language Models.
- Prompt engineering and AI summarisation.
- Managing API credentials securely.
- Building and extending AI-powered applications.

## 👩‍💻 Project Status

**Status:** Under Development

This project is being developed incrementally, with planned enhancements around RAG, AI agents, search evaluation and deployment.

---

**Built with Python, FastAPI, SerpAPI, Tavily and Google Gemini.**
