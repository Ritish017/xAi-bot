"""
Run the AI & Tech News Tweet Manager with actual publishing to X (Twitter).
"""
from app.main import app


def run_bot(niche: str = "AI and Tech"):
    """
    Run the AI & Tech News Tweet Manager with the specified niche.
    
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
    
    print("🤖 Running AI & Tech News Tweet Manager...")
    print(f"📌 Niche: {inputs['niche']}\n")
    
    result = app.invoke(inputs)
    
    if result.get('error'):
        print(f"\n❌ Error: {result['error']}")
        return result
    
    print("\n✅ Tweet published successfully!")
    print(f"\n📝 Content Idea:\n{result.get('content_idea', 'N/A')}\n")
    print(f"🐦 Final Tweet:\n{result.get('final_tweet', 'N/A')}\n")
    print(f"🎯 Hook Style: {result.get('hook_style', 'N/A')}")
    print(f"📊 Tweet Length: {len(result.get('final_tweet', ''))} characters")
    
    return result


if __name__ == "__main__":
    run_bot("AI and Tech")
