# 🤖 AI & Tech News Tweet Manager

An intelligent Twitter/X automation bot powered by **LangGraph**, **Google Gemini AI**, and **Tavily Search** that automatically researches the latest AI and Tech news globally and publishes viral tweets to X (Twitter).

## 🌟 What It Does

This bot automatically:
1. 🔍 **Searches** for the latest breaking AI & Tech news globally
2. 🧠 **Analyzes** the most exciting stories using AI
3. ✍️ **Generates** engaging, viral-worthy tweets
4. 🐦 **Publishes** directly to X/Twitter

Perfect for tech enthusiasts, AI developers, and content creators who want to stay on top of AI news and share it with their audience!

## 📁 Project Structure

```
xAi-bot/
├── app/
│   ├── config.py          # Configuration and environment variables
│   ├── models.py          # Data models (BotState)
│   ├── workflow.py        # LangGraph workflow definition
│   ├── main.py            # Main app instances
│   └── nodes/
│       ├── researcher.py  # AI & Tech news research node
│       ├── writer.py      # Tweet writing node
│       └── publisher.py   # X/Twitter publishing node
├── main.py                # CLI entry point
├── run_bot.py             # Production runner (with publishing)
├── test_bot.py            # Test runner (without publishing)
├── .env                   # Environment variables (API keys)
└── pyproject.toml         # Project dependencies
```

## 🚀 Features

- **🔍 AI-Powered Research**: Uses Tavily search to find the latest AI breakthroughs, model releases, tech announcements, and industry news
- **✨ Viral Tweet Generation**: Creates engaging, high-energy tweets with hooks, emojis, and relevant hashtags
- **📤 Automated Publishing**: Posts directly to X/Twitter with one command
- **🔄 LangGraph Workflow**: Structured multi-step AI agent workflow
- **🧪 Test Mode**: Preview tweets without publishing
- **⚡ Conditional Logic**: Smart validation and error handling

## 📋 Prerequisites

- Python 3.13+
- X (Twitter) API credentials (Developer Account)
- Google Gemini API key
- Tavily API key

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/xAi-bot.git
   cd xAi-bot
   ```

2. **Install dependencies**
   ```bash
   uv pip install -e .
   ```

3. **Set up environment variables**
   
   Create a `.env` file with:
   ```env
   # X (Twitter) API Credentials
   X_API_KEY=your_api_key
   X_API_SECRET=your_api_secret
   X_ACCESS_TOKEN=your_access_token
   X_ACCESS_SECRET=your_access_secret
   
   # Google Gemini API Key
   GEMINI_API_KEY=your_gemini_key
   
   # Tavily API Key
   TAVILY_API_KEY=your_tavily_key
   ```

## 💻 Usage

### Interactive Mode
```bash
python main.py
```

### Direct Mode - Test (No Publishing)
```bash
python main.py --test "AI and Tech"
```

### Direct Mode - Live Publishing
```bash
python main.py "AI and Tech"
```

### Using Scripts Directly

**Test mode (preview tweet, no publishing):**
```bash
python test_bot.py
```

**Live mode (publish to X/Twitter):**
```bash
python run_bot.py
```

## 🔄 LangGraph Workflow

The bot follows this intelligent LangGraph workflow:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Researcher │ ──▶ │ Tweet Writer │ ──▶ │  Publisher  │
│    Node     │     │     Node     │     │    Node     │
└─────────────┘     └──────────────┘     └─────────────┘
      │                                         │
      │         (Research Validation)           │
      └─────────────────────────────────────────┘
```

1. **🔍 Researcher Node**
   - Searches Tavily for latest AI & Tech news
   - Finds AI breakthroughs, model releases, tech announcements
   - Extracts key statistics and company names

2. **✍️ Writer Node**
   - Crafts viral tweets (< 280 chars)
   - Adds compelling hooks and CTAs
   - Includes relevant hashtags (#AI #TechNews #MachineLearning)

3. **📤 Publisher Node** *(Optional in test mode)*
   - Posts tweet to X/Twitter
   - Returns confirmation

## ⚙️ Configuration

Edit `app/config.py` to customize:

| Setting | Description | Default |
|---------|-------------|---------|
| `LLM_MODEL` | AI model to use | `gemini-2.5-flash` |
| `LLM_TEMPERATURE_RESEARCH` | Temperature for research | `0` (deterministic) |
| `LLM_TEMPERATURE_CREATIVE` | Temperature for writing | `0.7` (creative) |
| `MAX_SEARCH_RESULTS` | Number of search results | `3` |
| `MAX_TWEET_LENGTH` | Maximum tweet length | `280` |

## 🧪 Testing

Test the bot without publishing:

```bash
python test_bot.py
```

Or with a specific topic:

```bash
python main.py --test "OpenAI GPT-5"
```

## 📝 Example Output

```
🧪 Testing AI & Tech News Tweet Manager (No Publishing)...
📌 Niche: AI and Tech

✅ Test completed!

📝 Content Idea:
Breaking: OpenAI announces GPT-5 with revolutionary reasoning capabilities...

🐦 Final Tweet:
🚨 BREAKING: OpenAI just dropped GPT-5 and it's INSANE! 

New reasoning capabilities that outperform humans in complex tasks 🤯

This changes everything for AI development.

What do you think - are we ready for this? 👇

#AI #OpenAI #GPT5 #TechNews

📊 Tweet Length: 245 characters
```

## 🛠️ Tech Stack

- **LangGraph** - Workflow orchestration for AI agents
- **LangChain** - LLM framework
- **Google Gemini AI** - Content generation
- **Tavily Search** - Real-time news research
- **Tweepy** - X/Twitter API integration
- **Python 3.13+** - Modern Python

## 🛡️ Error Handling

- ✅ Research validation ensures quality content
- ✅ Graceful error messages
- ✅ Test mode for safe development
- ✅ SSL error handling for Windows

## 📦 Dependencies

```
langchain
langgraph
langchain-google-genai
langchain-community
tweepy
python-dotenv
tavily-python
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License

---

Made with ❤️ using LangGraph, Google Gemini AI, and Tavily Search

**🔗 Connect with me on LinkedIn to see this bot in action!**
