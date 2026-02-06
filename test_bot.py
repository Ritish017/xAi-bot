"""
Test the AI Tweet Bot without publishing to X (Twitter).
"""
from app.main import app_test


def test_bot(niche: str):
    """
    Test the AI Tweet Bot without publishing to X.
    
    Args:
        niche: The topic/niche for tweet generation
    """
    inputs = {"niche": niche, "content_idea": "", "final_tweet": "", "error": ""}
    
    print("🧪 Testing AI Tweet Bot (No Publishing)...")
    print(f"📌 Niche: {inputs['niche']}\n")
    
    result = app_test.invoke(inputs)
    
    if result.get('error'):
        print(f"\n❌ Error: {result['error']}")
        return result
    
    print("\n✅ Test completed!")
    print(f"\n📝 Content Idea:\n{result.get('content_idea', 'N/A')}\n")
    print(f"🐦 Final Tweet:\n{result.get('final_tweet', 'N/A')}\n")
    print(f"📊 Tweet Length: {len(result.get('final_tweet', ''))} characters")
    
    return result


if __name__ == "__main__":
    # Test with your desired niche
    test_bot("AI Agents in 2026")
