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
    inputs = {"niche": niche, "content_idea": "", "final_tweet": "", "error": ""}
    
    print("🤖 Running AI & Tech News Tweet Manager...")
    print(f"📌 Niche: {inputs['niche']}\n")
    
    result = app.invoke(inputs)
    
    if result.get('error'):
        print(f"\n❌ Error: {result['error']}")
        return result
    
    print("\n✅ Tweet published successfully!")
    print(f"\n📝 Content Idea:\n{result.get('content_idea', 'N/A')}\n")
    print(f"🐦 Final Tweet:\n{result.get('final_tweet', 'N/A')}\n")
    print(f"📊 Tweet Length: {len(result.get('final_tweet', ''))} characters")
    
    return result


if __name__ == "__main__":
    # Run with AI and Tech news niche
    run_bot("AI and Tech")
