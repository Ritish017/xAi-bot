"""
Publisher node: Posts the generated tweet to X (Twitter).
"""
import tweepy
from app.models import BotState
from app.config import Config


def publisher(state: BotState) -> dict:
    """
    Publisher node: Posts the generated tweet to X (Twitter).
    
    Args:
        state: Current bot state containing the final_tweet
        
    Returns:
        Updated state (unchanged if successful, with error if failed)
    """
    try:
        client = tweepy.Client(
            consumer_key=Config.X_API_KEY,
            consumer_secret=Config.X_API_SECRET,
            access_token=Config.X_ACCESS_TOKEN,
            access_token_secret=Config.X_ACCESS_SECRET
        )

        tweet = client.create_tweet(text=state['final_tweet'])
        print(f"✅ Tweet published successfully! Tweet ID: {tweet.data['id']}")
        return state
        
    except Exception as e:
        print(f"❌ Failed to publish tweet: {str(e)}")
        return {**state, "error": f"Publishing failed: {str(e)}"}
