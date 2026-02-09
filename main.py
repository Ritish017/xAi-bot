"""
AI & Tech News Tweet Manager - Entry Point
A LangGraph-powered bot that automatically generates and publishes viral tweets 
about the latest AI and Tech news to X (Twitter).

Usage:
    python main.py                    # Interactive mode
    python main.py "AI and Tech"      # Direct mode (live publishing)
    python main.py --test "AI and Tech" # Test mode (no publishing)
"""
import sys
from run_bot import run_bot
from test_bot import test_bot


def main():
    """Main entry point for the AI & Tech News Tweet Manager."""
    
    print("=" * 60)
    print("🤖 AI & Tech News Tweet Manager")
    print("   Powered by LangGraph & Google Gemini AI")
    print("=" * 60)
    
    # Default niche for AI & Tech news
    default_niche = "AI and Tech"
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test":
            niche = sys.argv[2] if len(sys.argv) > 2 else default_niche
            test_bot(niche)
        else:
            niche = sys.argv[1]
            run_bot(niche)
    else:
        # Interactive mode
        print("\n📰 Auto-tweet the latest AI & Tech news to X!")
        print("\nChoose mode:")
        print("1. Test mode (preview tweet, no publishing)")
        print("2. Live mode (publish to X/Twitter)")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        niche = input(f"Enter topic (press Enter for '{default_niche}'): ").strip()
        
        if not niche:
            niche = default_niche
        
        if choice == "1":
            test_bot(niche)
        elif choice == "2":
            confirm = input("\n⚠️  This will publish to X/Twitter. Continue? (yes/no): ").strip().lower()
            if confirm == "yes":
                run_bot(niche)
            else:
                print("❌ Cancelled.")
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
