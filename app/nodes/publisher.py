"""
Publisher node: Posts the generated tweet to X (Twitter).
Handles image upload (if available), deduplication logging, and analytics.
"""
import tweepy
import os
from app.models import BotState
from app.config import Config
from app.nodes.dedup import add_to_history
from app.nodes.analytics import log_tweet


def publisher(state: BotState) -> dict:
    """
    Publisher node: Posts the generated tweet to X (Twitter).
    If an image was generated, uploads it via V1.1 API and attaches to tweet.
    
    Args:
        state: Current bot state containing the final_tweet and optionally image_path
        
    Returns:
        Updated state (unchanged if successful, with error if failed)
    """
    try:
        # V2 API for tweeting
        client = tweepy.Client(
            consumer_key=Config.X_API_KEY,
            consumer_secret=Config.X_API_SECRET,
            access_token=Config.X_ACCESS_TOKEN,
            access_token_secret=Config.X_ACCESS_SECRET
        )

        media_id = None
        image_path = state.get('image_path', '')
        
        if image_path and os.path.exists(image_path):
            try:
                # V1.1 API for Media Upload
                auth = tweepy.OAuth1UserHandler(
                    Config.X_API_KEY, Config.X_API_SECRET,
                    Config.X_ACCESS_TOKEN, Config.X_ACCESS_SECRET
                )
                api = tweepy.API(auth)
                
                print(f"⬆️  Uploading image to X/Twitter...")
                media = api.media_upload(image_path)
                media_id = media.media_id
                print(f"✅ Image uploaded successfully! Media ID: {media_id}")
                
                # Clean up temp file
                os.remove(image_path)
            except Exception as e:
                print(f"⚠️  Image upload failed: {str(e)}. Posting without image.")
        
        # Post tweet (with or without image)
        if media_id:
            tweet = client.create_tweet(text=state['final_tweet'], media_ids=[media_id])
        else:
            tweet = client.create_tweet(text=state['final_tweet'])
            
        tweet_id = tweet.data['id']
        print(f"✅ Tweet published successfully! Tweet ID: {tweet_id}")
        
        # Log for deduplication
        add_to_history(
            topic_summary=state.get('content_idea', '')[:200],
            tweet_text=state['final_tweet']
        )
        
        # Log for analytics
        log_tweet(
            tweet_text=state['final_tweet'],
            hook_style=state.get('hook_style', 'unknown'),
            tweet_id=str(tweet_id),
            topic=state.get('content_idea', '')[:200]
        )
        
        return state
        
    except Exception as e:
        print(f"❌ Failed to publish tweet: {str(e)}")
        return {**state, "error": f"Publishing failed: {str(e)}"}
