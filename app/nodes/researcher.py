"""
Researcher node: Searches for trending topics and generates content ideas.
"""
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models import BotState
from app.config import Config


def researcher(state: BotState) -> dict:
    """
    Research node: Searches for trending topics in the specified niche.
    
    Args:
        state: Current bot state containing the niche
        
    Returns:
        Updated state with content_idea and error fields
    """
    search = TavilySearchResults(max_results=Config.MAX_SEARCH_RESULTS)
    query = f"latest trending news and updates for {state['niche']} February 2026"

    try:
        search_results = search.invoke(query)
        
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
            f"identify the most controversial or exciting trending story about {state['niche']}. "
            "Focus on things that trigger high engagement (debates, breaking news, or records). "
            "Also retrieve some statistical data to make the tweet more informative."
        )
        
        response = llm.invoke(prompt)
        return {"content_idea": response.content, "error": ""}
    
    except Exception as e:
        return {
            "content_idea": f"Research failed: {str(e)}",
            "error": f"Research error: {str(e)}"
        }
