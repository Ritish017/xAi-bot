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
    Falls back to AI-generated content if search fails.
    
    Args:
        state: Current bot state containing the niche
        
    Returns:
        Updated state with content_idea and error fields
    """
    niche = state['niche']
    search_results = None
    
    # Try Tavily search first
    try:
        search = TavilySearchResults(max_results=Config.MAX_SEARCH_RESULTS)
        query = f"latest trending news and updates for {niche} February 2026"
        search_results = search.invoke(query)
        print(f"✅ Tavily search returned {len(search_results) if search_results else 0} results")
    except Exception as e:
        print(f"⚠️ Tavily search failed: {str(e)}")
        search_results = None

    # Generate content with AI
    try:
        llm = ChatGoogleGenerativeAI(
            model=Config.LLM_MODEL,
            temperature=Config.LLM_TEMPERATURE_RESEARCH
        )

        if search_results:
            # Use search results
            prompt = (
                f"Based on these search results: {search_results}, "
                f"identify the most controversial or exciting trending story about {niche}. "
                "Focus on things that trigger high engagement (debates, breaking news, or records). "
                "Also include some statistical data to make the tweet more informative."
            )
        else:
            # Fallback: Generate content without search
            prompt = (
                f"You are a cricket expert. Generate an exciting, trending insight about {niche}. "
                "Think about: current match updates, player performances, team rankings, "
                "controversial decisions, record-breaking moments, or upcoming key matches. "
                "Make it sound like breaking news that would engage cricket fans. "
                "Include realistic statistics or facts."
            )
            print("📝 Using AI-generated content (no search results)")
        
        response = llm.invoke(prompt)
        content = response.content
        
        if content and len(content) > 50:
            print(f"✅ Content generated: {len(content)} characters")
            return {"content_idea": content, "error": ""}
        else:
            return {"content_idea": "", "error": "Generated content too short"}
    
    except Exception as e:
        print(f"❌ Content generation failed: {str(e)}")
        return {
            "content_idea": "",
            "error": f"Research error: {str(e)}"
        }
