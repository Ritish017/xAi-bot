"""
Test the AI & Tech News Tweet Manager without publishing to X (Twitter).
Logs analytics even in test mode for tracking.
"""
from app.main import app_test
from app.nodes.dedup import add_to_history
from app.nodes.analytics import log_tweet


def test_bot(niche: str = "AI and Tech"):
    """
    Test the AI & Tech News Tweet Manager without publishing to X.
    
    Args:
        niche: The topic/niche for tweet generation (default: AI and Tech)
    """
    inputs = {
        "niche": niche,
        "content_idea": "",
        "final_tweet": "",
        "hook_style": "",
        "image_prompt": "",
        "image_url": "",
        "image_path": "",
        "error": ""
    }
    
    print("🧪 Testing AI & Tech News Tweet Manager (No Publishing)...")
    print(f"📌 Niche: {inputs['niche']}\n")
    
    result = app_test.invoke(inputs)
    
    if result.get('error'):
        print(f"\n❌ Error: {result['error']}")
        return result
    
    print("\n✅ Test completed!")
    print(f"\n📝 Content Idea:\n{result.get('content_idea', 'N/A')}\n")
    print(f"🐦 Final Tweet:\n{result.get('final_tweet', 'N/A')}\n")
    print(f"🎯 Hook Style: {result.get('hook_style', 'N/A')}")
    print(f"📊 Tweet Length: {len(result.get('final_tweet', ''))} characters")
    
    # Log dedup and analytics even in test mode
    if result.get('final_tweet') and 'failed' not in result.get('final_tweet', '').lower():
        add_to_history(
            topic_summary=result.get('content_idea', '')[:200],
            tweet_text=result['final_tweet']
        )
        log_tweet(
            tweet_text=result['final_tweet'],
            hook_style=result.get('hook_style', 'unknown'),
            tweet_id="TEST",
            topic=result.get('content_idea', '')[:200]
        )
        print("\n📋 Logged to tweet_history.json and tweet_log.csv")
    
    return result


if __name__ == "__main__":
    test_bot("AI and Tech")
