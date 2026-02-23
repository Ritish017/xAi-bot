"""
Data models for the AI & Tech News Tweet Manager.
"""
from typing import TypedDict


class BotState(TypedDict):
    """State object that flows through the LangGraph workflow."""
    niche: str
    content_idea: str
    final_tweet: str
    hook_style: str
    image_prompt: str
    image_url: str
    image_path: str   # Local temp file path for generated image
    error: str
