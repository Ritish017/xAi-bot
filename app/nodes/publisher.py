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
        # Debug: Check if credentials are loaded with more details
        print(f"\n� Publisher Node:")
        print(f"   API Key loaded: {'Yes' if Config.X_API_KEY else 'NO!'} (len: {len(Config.X_API_KEY) if Config.X_API_KEY else 0})")
        print(f"   API Secret loaded: {'Yes' if Config.X_API_SECRET else 'NO!'} (len: {len(Config.X_API_SECRET) if Config.X_API_SECRET else 0})")
        print(f"   Access Token loaded: {'Yes' if Config.X_ACCESS_TOKEN else 'NO!'} (len: {len(Config.X_ACCESS_TOKEN) if Config.X_ACCESS_TOKEN else 0})")
        print(f"   Access Secret loaded: {'Yes' if Config.X_ACCESS_SECRET else 'NO!'} (len: {len(Config.X_ACCESS_SECRET) if Config.X_ACCESS_SECRET else 0})")
        
        # Check for whitespace issues in credentials
        if Config.X_API_KEY and Config.X_API_KEY != Config.X_API_KEY.strip():
            print(f"   ⚠️ WARNING: API Key has leading/trailing whitespace!")
        if Config.X_ACCESS_TOKEN and Config.X_ACCESS_TOKEN != Config.X_ACCESS_TOKEN.strip():
            print(f"   ⚠️ WARNING: Access Token has leading/trailing whitespace!")
        
        # Check tweet content
        tweet_text = state.get('final_tweet', '').strip()
        print(f"📝 Tweet length: {len(tweet_text)} characters")
        
        if not tweet_text:
            return {**state, "error": "No tweet content to publish"}
        
        # Truncate if too long
        if len(tweet_text) > 280:
            tweet_text = tweet_text[:277] + "..."
            print(f"   ⚠️ Tweet truncated to 280 characters")
        
        # Strip whitespace from credentials (common issue)
        client = tweepy.Client(
            consumer_key=Config.X_API_KEY.strip() if Config.X_API_KEY else None,
            consumer_secret=Config.X_API_SECRET.strip() if Config.X_API_SECRET else None,
            access_token=Config.X_ACCESS_TOKEN.strip() if Config.X_ACCESS_TOKEN else None,
            access_token_secret=Config.X_ACCESS_SECRET.strip() if Config.X_ACCESS_SECRET else None
        )
        
        # Verify credentials by getting authenticated user
        print(f"   🔍 Verifying credentials...")
        me = client.get_me()
        if me.data:
            print(f"   ✅ Authenticated as: @{me.data.username}")
        else:
            print(f"   ⚠️ Could not verify user identity")

        tweet = client.create_tweet(text=tweet_text)
        print(f"✅ Tweet published successfully! Tweet ID: {tweet.data['id']}")
        return state
        
    except tweepy.Unauthorized as e:
        print(f"❌ 401 Unauthorized: Check your API credentials!")
        print(f"   - Make sure App has 'Read and Write' permissions")
        print(f"   - Regenerate Access Token AFTER changing permissions")
        return {**state, "error": f"Twitter Auth Error: {str(e)}"}
        
    except tweepy.Forbidden as e:
        print(f"❌ 403 Forbidden: App doesn't have write permissions!")
        print(f"   - Go to Developer Portal → App Settings")
        print(f"   - Enable 'Read and Write' in User Authentication")
        return {**state, "error": f"Twitter Permission Error: {str(e)}"}
        
    except Exception as e:
        print(f"❌ Failed to publish tweet: {str(e)}")
        return {**state, "error": f"Publishing failed: {str(e)}"}
