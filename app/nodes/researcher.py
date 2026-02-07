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
        
        # Count results properly
        if isinstance(search_results, list):
            result_count = len(search_results)
        else:
            result_count = 1 if search_results else 0
        
        print(f"✅ Tavily search returned {result_count} results (max: {Config.MAX_SEARCH_RESULTS})")
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
            # Use search results - extract specific facts
            prompt = f"""Analyze these search results about {niche}:

{search_results}

Extract and summarize the KEY FACTS for a tweet:
1. PLAYER NAMES mentioned (full names)
2. SCORES or STATISTICS (exact numbers)
3. MATCH DETAILS (teams, venue, date)
4. Any CONTROVERSY or BREAKING NEWS

Format your response as bullet points with SPECIFIC data only.
Do NOT use placeholders like [Player] - only include real data you found.
If a piece of information is not in the search results, skip it."""
        else:
            # Fallback: Generate content without search
            prompt = f"""You are a cricket journalist covering {niche}.

Generate a realistic, specific cricket update that could be tweeted.
Include:
- Real player names from current teams (India, Australia, England, etc.)
- Realistic match scores or statistics
- Current tournament context

Make it sound like breaking news. Be specific with names and numbers."""
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
