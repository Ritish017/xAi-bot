"""
Analytics logging for the AI & Tech News Tweet Manager.
Logs every tweet to a CSV file for tracking performance over time.
"""
import csv
import os
from datetime import datetime
from app.config import Config


def log_tweet(tweet_text: str, hook_style: str, tweet_id: str = "", topic: str = "") -> None:
    """
    Log a tweet to the analytics CSV file.
    
    Args:
        tweet_text: The full tweet text
        hook_style: Which hook style was used (breaking, question, etc.)
        tweet_id: The X/Twitter tweet ID (empty for test runs)
        topic: Brief topic summary
    """
    file_exists = os.path.exists(Config.TWEET_LOG_FILE)
    
    with open(Config.TWEET_LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Write header if file is new
        if not file_exists:
            writer.writerow([
                "timestamp", "tweet_text", "char_count", 
                "hook_style", "tweet_id", "topic"
            ])
        
        writer.writerow([
            datetime.now().isoformat(),
            tweet_text,
            len(tweet_text),
            hook_style,
            tweet_id,
            topic[:200] if topic else "",
        ])
