"""
Hook styles for viral tweet generation.
Rotating between different hook formats to prevent the account from looking
repetitive and to maximize engagement across different audience segments.

Based on X's 2025 recommendation algorithm research:
- Replies > Bookmarks > Reposts > Likes (engagement weighting)
- No external links (50-90% reach penalty)
- 1-2 hashtags max
- Conversational CTAs drive replies (highest-weighted signal)
"""
import random


# Each hook style defines a tweet structure template and a matching CTA pool
HOOK_STYLES = [
    {
        "name": "breaking",
        "instruction": (
            "Start with '🚨 BREAKING:' followed by the most shocking fact from the news. "
            "Make it sound urgent and time-sensitive. Use present tense."
        ),
        "cta_pool": [
            "This changes everything. Thoughts?",
            "Are we ready for this?",
            "The future is HERE. What's your take?",
            "This is massive. Agree or disagree?",
        ],
    },
    {
        "name": "question",
        "instruction": (
            "Start with a thought-provoking question that makes people stop scrolling. "
            "The question should challenge conventional wisdom or present a dilemma. "
            "Then answer it with the news fact."
        ),
        "cta_pool": [
            "What would YOU do with this?",
            "Drop your prediction below 👇",
            "Hot take or cold truth?",
            "Tell me I'm wrong 👇",
        ],
    },
    {
        "name": "bold_stat",
        "instruction": (
            "Lead with the most jaw-dropping statistic or number from the news. "
            "Use $ amounts, percentages, or scale comparisons. "
            "Format: '[SHOCKING NUMBER] — here's why it matters:'"
        ),
        "cta_pool": [
            "Let that satisfying number sink in. Thoughts?",
            "Mind blown? Same. React below 👇",
            "Save this for later 🔖",
            "The numbers don't lie. What do you think?",
        ],
    },
    {
        "name": "hot_take",
        "instruction": (
            "Start with a bold, slightly controversial opinion or prediction about the news. "
            "Take a strong stance. Be provocative but factual. "
            "Format: 'Unpopular opinion:' or 'Hot take:' or a bold declarative statement."
        ),
        "cta_pool": [
            "Fight me on this 👇",
            "Am I wrong? Tell me below.",
            "Agree or disagree? RT if you agree 🔄",
            "Change my mind 👇",
        ],
    },
    {
        "name": "thread_opener",
        "instruction": (
            "Write as if opening a viral thread — but pack everything into one tweet. "
            "Start with 'Here's why [topic] changes everything:' or 'Everyone's sleeping on this:'. "
            "Create FOMO and urgency."
        ),
        "cta_pool": [
            "Follow for more AI insights 🧠",
            "Bookmark this before everyone catches on 🔖",
            "RT to spread the word 🔄",
            "Who else is paying attention to this?",
        ],
    },
]


def get_random_hook() -> dict:
    """Select a random hook style and CTA for tweet generation."""
    hook = random.choice(HOOK_STYLES)
    cta = random.choice(hook["cta_pool"])
    return {
        "name": hook["name"],
        "instruction": hook["instruction"],
        "cta": cta,
    }
