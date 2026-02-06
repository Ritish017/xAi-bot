"""
Writer node: Generates viral tweets based on researched content.
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models import BotState
from app.config import Config


def tweet_writer(state: BotState) -> dict:
    """
    Writer node: Generates a viral tweet based on researched content.
    
    Args:
        state: Current bot state containing the content_idea
        
    Returns:
        Updated state with final_tweet field
    """
    llm = ChatGoogleGenerativeAI(
        model=Config.LLM_MODEL,
        temperature=Config.LLM_TEMPERATURE_CREATIVE
    )
    
    prompt = (
        f"Context: {state['content_idea']}\n\n"
        f"Think of yourself as a top-tier social media marketer specializing in "
        f"crafting viral tweets for the {state['niche']} community.\n"
        f"Task: Write a viral X tweet for the {state['niche']} community.\n"
        "Guidelines:\n"
        "1. Start with a massive HOOK (Question, bold statement, or 'Breaking').\n"
        f"2. Keep it under {Config.MAX_TWEET_LENGTH} chars.\n"
        "3. Use 2-3 trending hashtags.\n"
        "4. Include emojis and a 'Call to Action' (e.g., 'What do you think?').\n"
        "5. Tone: High energy/Opinionated."
    )
    
    try:
        response = llm.invoke(prompt)
        return {"final_tweet": response.content}
    except Exception as e:
        return {"final_tweet": f"Tweet generation failed: {str(e)}"}
