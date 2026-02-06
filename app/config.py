"""
Configuration module for the AI Tweet Bot.
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
    
    # Google Gemini API Key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # Tavily API Key
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    # LLM Settings
    LLM_MODEL = "gemini-2.5-flash"
    LLM_TEMPERATURE_RESEARCH = 0
    LLM_TEMPERATURE_CREATIVE = 0.7
    
    # Search Settings
    MAX_SEARCH_RESULTS = 3
    
    # Tweet Settings
    MAX_TWEET_LENGTH = 280
