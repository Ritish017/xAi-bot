"""
Workflow definition for the AI & Tech News Tweet Manager using LangGraph.
"""
from langgraph.graph import StateGraph, START, END
from app.models import BotState
from app.nodes import researcher, tweet_writer, publisher


def validate_research(state: BotState) -> str:
    """
    Conditional edge: Checks if the researcher found useful content.
    
    Args:
        state: Current bot state
        
    Returns:
        "pass" if research was successful, "fail" otherwise
    """
    error = state.get("error", "")
    content = state.get("content_idea", "")

    if error or "failed" in content.lower() or not content:
        print("⚠️ Research validation failed. Stopping workflow.")
        return "fail"
    
    return "pass"


def create_workflow(include_publisher: bool = True):
    """
    Creates the LangGraph workflow for the tweet bot.
    
    Args:
        include_publisher: Whether to include the publisher node (set False for testing)
        
    Returns:
        Compiled LangGraph workflow
    """
    workflow = StateGraph(BotState)
    
    # Add nodes
    workflow.add_node("researcher", researcher)
    workflow.add_node("tweet_writer", tweet_writer)
    
    if include_publisher:
        workflow.add_node("publisher", publisher)
    
    # Add edges
    workflow.add_edge(START, "researcher")
    workflow.add_conditional_edges(
        "researcher",
        validate_research,
        {
            "pass": "tweet_writer",
            "fail": END
        }
    )
    
    if include_publisher:
        workflow.add_edge("tweet_writer", "publisher")
        workflow.add_edge("publisher", END)
    else:
        workflow.add_edge("tweet_writer", END)
    
    return workflow.compile()
