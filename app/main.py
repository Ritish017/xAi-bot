"""
AI Tweet Bot - Main Application
Generates and publishes viral tweets using LangGraph and AI.
"""
from app.workflow import create_workflow

# Create the main app with publisher enabled
app = create_workflow(include_publisher=True)

# Create a test app without publisher (for testing)
app_test = create_workflow(include_publisher=False)

