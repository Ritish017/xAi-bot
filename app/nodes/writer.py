"""
Writer node: Generates viral AI & Tech news tweets optimized for X's 2025
recommendation algorithm. Uses rotating hook styles and conversational CTAs
to maximize replies, bookmarks, and reposts.

X Algorithm Optimization:
- Replies > Bookmarks > Reposts > Likes (engagement weighting)
- NO external links (50-90% reach penalty)
- 1-2 hashtags max (more = spammy)
- 200-260 char sweet spot
- Conversational CTAs to drive replies (highest-weighted signal)
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from app.models import BotState
from app.config import Config
from app.nodes.hook_styles import get_random_hook


def tweet_writer(state: BotState) -> dict:
    """
    Writer node: Generates a viral tweet optimized for X's algorithm.

    Args:
        state: Current bot state containing the content_idea

    Returns:
        Updated state with final_tweet, hook_style, image_prompt, and image_url
    """
    llm = ChatGoogleGenerativeAI(
        model=Config.LLM_MODEL,
        temperature=Config.LLM_TEMPERATURE_CREATIVE,
        google_api_key=Config.GEMINI_API_KEY
    )

    # Get a random hook style for variety
    hook = get_random_hook()
    hook_name = hook["name"]
    hook_instruction = hook["instruction"]
    hook_cta = hook["cta"]

    print(f"✍️  Generating viral tweet (hook: {hook_name})...")

    tweet_prompt = (
        f"Context: {state['content_idea']}\n\n"
        f"You are a top-tier tech influencer crafting a viral tweet about {state['niche']} news.\n\n"
        f"HOOK STYLE: {hook_instruction}\n\n"
        f"MANDATORY RULES (X Algorithm Optimization 2025):\n"
        f"1. NEVER include any URLs, links, or website addresses. X penalizes links with 50-90% less reach.\n"
        f"2. Keep tweet between {Config.TWEET_SWEET_SPOT_MIN}-{Config.TWEET_SWEET_SPOT_MAX} characters (sweet spot for engagement).\n"
        f"3. MUST be under {Config.MAX_TWEET_LENGTH} characters total (HARD LIMIT).\n"
        f"4. Use maximum 2 hashtags, placed at the END of the tweet.\n"
        f"5. Use 2-3 relevant emojis to increase visual appeal.\n"
        f"6. End the tweet with this call-to-action: \"{hook_cta}\"\n"
        f"7. The CTA drives REPLIES — the #1 ranking signal in X's algorithm.\n"
        f"8. Make the content worth BOOKMARKING (unique insight, surprising stat).\n"
        f"9. Tone: Exciting, mind-blowing, authoritative — like a tech insider dropping alpha.\n"
        f"10. Return ONLY the tweet text, absolutely nothing else. No quotes, no labels, no prefix."
    )

    try:
        tweet_response = llm.invoke(tweet_prompt)
        final_tweet = tweet_response.content.strip()
        
        # Remove any surrounding quotes the LLM might add
        if final_tweet.startswith('"') and final_tweet.endswith('"'):
            final_tweet = final_tweet[1:-1]
        if final_tweet.startswith("'") and final_tweet.endswith("'"):
            final_tweet = final_tweet[1:-1]

        # Enforce character limit as a hard safety net
        if len(final_tweet) > Config.MAX_TWEET_LENGTH:
            # Try to cut at last complete sentence/phrase
            truncated = final_tweet[:Config.MAX_TWEET_LENGTH]
            # Find last period, question mark, or exclamation
            for char in ['. ', '? ', '! ']:
                last_idx = truncated.rfind(char)
                if last_idx > Config.TWEET_SWEET_SPOT_MIN:
                    final_tweet = truncated[:last_idx + 1]
                    break
            else:
                # Fall back to word boundary
                final_tweet = truncated.rsplit(" ", 1)[0]

        print(f"✅ Tweet generated ({len(final_tweet)} chars, hook: {hook_name})")

        return {
            "final_tweet": final_tweet,
            "hook_style": hook_name,
            "image_prompt": "",  # Image generation disabled
            "image_url": "",     # Image generation disabled
        }

    except Exception as e:
        print(f"❌ Writer error: {str(e)}")
        return {
            "final_tweet": f"Tweet generation failed: {str(e)}",
            "hook_style": hook_name,
            "image_prompt": "",
            "image_url": "",
        }
