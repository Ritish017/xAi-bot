"""
Researcher node: Searches for latest AI and Tech news globally.
"""
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models import BotState
from app.config import Config


def researcher(state: BotState) -> dict:
    """
    Research node: Searches for latest AI and Tech news globally.
    
    Args:
        state: Current bot state containing the niche
        
    Returns:
        Updated state with content_idea and error fields
    """
    # Initialize Tavily Search with proper parameters
    search = TavilySearch(
        max_results=Config.MAX_SEARCH_RESULTS,
        topic="news",  # Use "news" topic for latest news
        include_answer=False,
        include_raw_content=True,
        include_images=False,
        search_depth="advanced",  # Use advanced for better results
        time_range="day"  # Get news from the last day
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
        
        llm = ChatGoogleGenerativeAI(
            model=Config.LLM_MODEL,
            temperature=Config.LLM_TEMPERATURE_RESEARCH
        )

        prompt = (
            f"Based on these search results: {search_results}, "
            f"identify the most exciting or breaking news about {state['niche']}. "
            "Focus on: AI breakthroughs, new model releases, tech company announcements, "
            "funding rounds, product launches, or industry-changing developments. "
            "Include relevant statistics, company names, and key details to make the tweet informative and engaging."
        )
        
        response = llm.invoke(prompt)
        return {"content_idea": response.content, "error": ""}
    
    except Exception as e:
        return {
            "content_idea": f"Research failed: {str(e)}",
            "error": f"Research error: {str(e)}"
        }
