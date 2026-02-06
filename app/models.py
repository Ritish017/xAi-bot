"""
Data models for the AI Tweet Bot.
"""
from typing import TypedDict


class BotState(TypedDict):
    """State object that flows through the LangGraph workflow."""
    niche: str
    content_idea: str
    final_tweet: str
    error: str
