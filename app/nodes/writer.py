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
    
    prompt = f"""You are a cricket journalist writing viral tweets about {state['niche']}.

RESEARCH DATA (use this information):
{state['content_idea']}

STRICT RULES:
1. ONLY use REAL names, scores, and facts from the research data above
2. NEVER use placeholders like [Player Name] or [Score] - use ACTUAL data
3. If research mentions a player, USE THEIR REAL NAME
4. If research mentions a score, USE THE ACTUAL SCORE
5. If you don't have specific data, focus on what you DO have

TWEET FORMAT:
- Start with a hook: 🚨 BREAKING, 🔥 or a bold question
- Include 1-2 specific facts (player names, scores, match details)
- Add 2-3 hashtags: #CricketWorldCup2026 #T20WorldCup
- End with engagement question
- MUST be under {Config.MAX_TWEET_LENGTH} characters
- Use emojis sparingly (2-3 max)

Write ONE tweet now. No explanations, just the tweet text:"""
    
    try:
        response = llm.invoke(prompt)
        tweet = response.content.strip()
        
        # Remove any markdown formatting that might be in the response
        tweet = tweet.replace('**', '').replace('*', '')
        
        # Remove quotes if the AI wrapped the tweet in them
        if tweet.startswith('"') and tweet.endswith('"'):
            tweet = tweet[1:-1]
        if tweet.startswith("'") and tweet.endswith("'"):
            tweet = tweet[1:-1]
            
        print(f"   ✅ Generated tweet: {len(tweet)} chars")
        return {"final_tweet": tweet}
    except Exception as e:
        print(f"   ❌ Tweet generation failed: {str(e)}")
        return {"final_tweet": f"Tweet generation failed: {str(e)}"}
