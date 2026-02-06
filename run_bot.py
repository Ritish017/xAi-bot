"""
Run the AI Tweet Bot with actual publishing to X (Twitter).
"""
from app.main import app


def run_bot(niche: str):
    """
    Run the AI Tweet Bot with the specified niche.
    
    Args:
        niche: The topic/niche for tweet generation
    """
    inputs = {"niche": niche, "content_idea": "", "final_tweet": "", "error": ""}
    
    print("🤖 Running AI Tweet Bot...")
    print(f"📌 Niche: {inputs['niche']}\n")
    
    result = app.invoke(inputs)
    
    if result.get('error'):
        print(f"\n❌ Error: {result['error']}")
        return result
    
    print("\n✅ Bot execution completed!")
    print(f"\n📝 Content Idea:\n{result.get('content_idea', 'N/A')}\n")
    print(f"🐦 Final Tweet:\n{result.get('final_tweet', 'N/A')}\n")
    print(f"📊 Tweet Length: {len(result.get('final_tweet', ''))} characters")
    
    return result


if __name__ == "__main__":
    # Run with your desired niche
    run_bot("AI Agents in 2026")
