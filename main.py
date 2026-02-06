"""
AI Tweet Bot - Entry Point
A LangGraph-powered bot that generates and publishes viral tweets using AI.

Usage:
    python main.py                    # Interactive mode
    python main.py "Your Niche"       # Direct mode
    python main.py --test "Your Niche" # Test mode (no publishing)
"""
import sys
from run_bot import run_bot
from test_bot import test_bot


def main():
    """Main entry point for the AI Tweet Bot."""
    
    print("=" * 60)
    print("🤖 AI Tweet Bot - Powered by LangGraph & AI")
    print("=" * 60)
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--test" and len(sys.argv) > 2:
            niche = sys.argv[2]
            test_bot(niche)
        else:
            niche = sys.argv[1]
            run_bot(niche)
    else:
        # Interactive mode
        print("\nChoose mode:")
        print("1. Test mode (no publishing)")
        print("2. Live mode (publish to X/Twitter)")
        
        choice = input("\nEnter choice (1 or 2): ").strip()
        niche = input("Enter your niche/topic: ").strip()
        
        if not niche:
            print("❌ Niche cannot be empty!")
            return
        
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
