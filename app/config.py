"""
Configuration module for the AI & Tech News Tweet Manager.
Loads environment variables and defines constants.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Application configuration settings."""
    
    # X (Twitter) API Credentials
    X_API_KEY = os.getenv("X_API_KEY")
    X_API_SECRET = os.getenv("X_API_SECRET")
    X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
    X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
    X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
    
    # Google Gemini API Key (for tweet/research generation)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # Separate Gemini API Key (for image generation only — avoids rate limits)
    GEMINI_IMAGE_API_KEY = os.getenv("GEMINI_IMAGE_API_KEY")
    
    # Tavily API Key
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    # LLM Settings
    LLM_MODEL = "gemini-2.5-flash"
    LLM_TEMPERATURE_RESEARCH = 0
    LLM_TEMPERATURE_CREATIVE = 0.9  # Higher creativity for viral tweets
    
    # Search Settings
    MAX_SEARCH_RESULTS = 3
    
    # Tweet Settings
    MAX_TWEET_LENGTH = 280
    TWEET_SWEET_SPOT_MIN = 200  # Optimal engagement range
    TWEET_SWEET_SPOT_MAX = 260
    
    # Image Generation (re-enabled with separate API key)
    ENABLE_IMAGE_GENERATION = True
    IMAGE_MODEL = "gemini-2.5-flash-image"  # Nano Banana (fast, free tier)
    
    # Deduplication
    TWEET_HISTORY_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tweet_history.json")
    MAX_HISTORY_SIZE = 100
    
    # Analytics
    TWEET_LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tweet_log.csv")
