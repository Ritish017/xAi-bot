"""
Deduplication system for the AI & Tech News Tweet Manager.
Prevents the bot from tweeting about the same news topic twice
by maintaining a rolling history of recent topics.
"""
import json
import os
from datetime import datetime
from app.config import Config


def load_history() -> list:
    """Load tweet history from JSON file."""
    if not os.path.exists(Config.TWEET_HISTORY_FILE):
        return []
    try:
        with open(Config.TWEET_HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_history(history: list) -> None:
    """Save tweet history to JSON file, keeping only the last MAX_HISTORY_SIZE entries."""
    # Trim to max size
    trimmed = history[-Config.MAX_HISTORY_SIZE:]
    with open(Config.TWEET_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(trimmed, f, indent=2, ensure_ascii=False)


def add_to_history(topic_summary: str, tweet_text: str) -> None:
    """Add a new topic to the history after successful tweet generation."""
    history = load_history()
    history.append({
        "timestamp": datetime.now().isoformat(),
        "topic": topic_summary[:200],  # Truncate for storage
        "tweet": tweet_text[:300],
    })
    save_history(history)


def get_recent_topics(limit: int = 20) -> str:
    """
    Get a formatted string of recent topics to feed to the LLM
    so it avoids repeating them.
    """
    history = load_history()
    recent = history[-limit:]
    if not recent:
        return "No previous tweets yet."
    
    topics = []
    for entry in recent:
        topics.append(f"- [{entry.get('timestamp', 'N/A')}] {entry.get('topic', 'N/A')}")
    
    return "\n".join(topics)
