"""
Cricket World Cup Tweet Bot - GitHub Actions Runner
Automatically generates and posts cricket-related tweets.
"""
import os
import sys
from datetime import datetime, timezone

def calculate_ist_hour():
    """Calculate current hour in IST (UTC+5:30)"""
    utc_now = datetime.now(timezone.utc)
    ist_offset_hours = 5.5
    ist_hour = (utc_now.hour + int(ist_offset_hours)) % 24
    return ist_hour

def determine_niche():
    """
    Returns appropriate niche based on time of day in IST.
    Morning: Match previews
    Afternoon: Live updates  
    Evening: Results & highlights
    """
    ist_hour = calculate_ist_hour()
    
    base_topic = "Cricket World Cup 2026"
    
    if ist_hour < 12:
        return f"{base_topic} - Match Preview & Team Analysis"
    elif ist_hour < 18:
        return f"{base_topic} - Live Match Updates"
    else:
        return f"{base_topic} - Match Results & Top Performances"

def execute_tweet_bot():
    """Main execution function for the tweet bot."""
    from app.main import app
    
    # Get niche from environment or determine dynamically
    niche = os.getenv("NICHE") or determine_niche()
    
    bot_input = {
        "niche": niche,
        "content_idea": "",
        "final_tweet": "",
        "error": ""
    }
    
    separator = "=" * 50
    
    print(f"\n{separator}")
    print("🏏 CRICKET WORLD CUP TWEET BOT")
    print(separator)
    print(f"📌 Topic: {niche}")
    print(f"🕐 UTC: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🇮🇳 IST Hour: ~{calculate_ist_hour()}:00")
    print(separator + "\n")
    
    try:
        result = app.invoke(bot_input)
        
        if result.get('error'):
            print(f"❌ Bot Error: {result['error']}")
            sys.exit(1)
        
        tweet_content = result.get('final_tweet', '')
        tweet_length = len(tweet_content)
        
        print(f"\n{separator}")
        print("✅ TWEET GENERATED & POSTED SUCCESSFULLY!")
        print(separator)
        print(f"\n🐦 Tweet Content:\n{tweet_content}")
        print(f"\n📏 Character Count: {tweet_length}/280")
        print(separator + "\n")
        
        return 0
        
    except Exception as error:
        print(f"\n❌ Critical Failure: {str(error)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    execute_tweet_bot()
