"""
Researcher node: Searches for latest AI and Tech news globally.
Includes deduplication to avoid repeating recent topics.
"""
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models import BotState
from app.config import Config
from app.nodes.dedup import get_recent_topics


def researcher(state: BotState) -> dict:
    """
    Research node: Searches for latest AI and Tech news globally.
    Uses deduplication to ensure fresh content every time.
    
    Args:
        state: Current bot state containing the niche
        
    Returns:
        Updated state with content_idea and error fields
    """
    # Initialize Tavily Search with proper parameters
    search = TavilySearch(
        max_results=Config.MAX_SEARCH_RESULTS,
        topic="news",
        include_answer=False,
        include_raw_content=True,
        include_images=False,
        search_depth="advanced",
        time_range="day"
    )
    
    query = f"latest breaking {state['niche']} news today artificial intelligence machine learning tech startups"

    try:
        # Invoke search with the query
        search_results = search.invoke({"query": query})
        
        if not search_results:
            return {
                "content_idea": "No search results found", 
                "error": "Search returned no results"
            }
        
        # Get recent topics to avoid duplication
        recent_topics = get_recent_topics(limit=20)
        
        llm = ChatGoogleGenerativeAI(
            model=Config.LLM_MODEL,
            temperature=Config.LLM_TEMPERATURE_RESEARCH,
            google_api_key=Config.GEMINI_API_KEY
        )

        prompt = (
            f"Based on these search results: {search_results}, "
            f"identify the single most ground-breaking, viral-worthy, and mind-blowing news about {state['niche']}. "
            "Focus strictly on: Massive AI breakthroughs, disruptive new model releases, shocking tech company announcements, "
            "or paradigm-shifting developments. "
            "Extract the most jaw-dropping facts, relevant statistics, company names, and key details. "
            "Provide a highly engaging summary that emphasizes the 'wow' factor and why people should care right now.\n\n"
            "CRITICAL RULES:\n"
            "1. Do NOT include any URLs, links, or website addresses in your response.\n"
            "2. Do NOT mention source websites or article URLs.\n"
            "3. Focus purely on the NEWS CONTENT — facts, stats, and impact.\n\n"
            f"AVOID these recently covered topics (pick something DIFFERENT):\n{recent_topics}"
        )
        
        response = llm.invoke(prompt)
        return {"content_idea": response.content, "error": ""}
    
    except Exception as e:
        return {
            "content_idea": f"Research failed: {str(e)}",
            "error": f"Research error: {str(e)}"
        }
