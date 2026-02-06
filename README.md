# 🤖 AI Tweet Bot

An intelligent Twitter/X bot powered by LangGraph, Google Gemini AI, and Tavily search that generates and publishes viral tweets automatically.

## 📁 Project Structure

```
xAi-bot/
├── app/
│   ├── config.py          # Configuration and environment variables
│   ├── models.py          # Data models (BotState)
│   ├── workflow.py        # LangGraph workflow definition
│   ├── main.py            # Main app instances
│   └── nodes/
│       ├── researcher.py  # Research node (Tavily search)
│       ├── writer.py      # Tweet writing node
│       └── publisher.py   # X/Twitter publishing node
├── main.py                # CLI entry point
├── run_bot.py             # Production runner (with publishing)
├── test_bot.py            # Test runner (without publishing)
├── .env                   # Environment variables (API keys)
└── pyproject.toml         # Project dependencies
```

## 🚀 Features

- **AI-Powered Research**: Uses Tavily search to find trending topics
- **Viral Tweet Generation**: Creates engaging, high-energy tweets with hooks and CTAs
- **Automated Publishing**: Posts directly to X/Twitter
- **LangGraph Workflow**: Structured multi-step AI agent workflow
- **Test Mode**: Test without publishing to X
- **Conditional Logic**: Smart validation and error handling

## 📋 Prerequisites

- Python 3.13+
- X (Twitter) API credentials
- Google Gemini API key
- Tavily API key

## 🔧 Installation

1. **Clone the repository**
   ```bash
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

### Direct Mode (Test)
```bash
python main.py --test "AI Agents in 2026"
```

### Direct Mode (Live Publishing)
```bash
python main.py "AI Agents in 2026"
```

### Using Scripts Directly

**Test mode (no publishing):**
```bash
python test_bot.py
```

**Live mode (with publishing):**
```bash
python run_bot.py
```

## 🔄 Workflow

The bot follows this LangGraph workflow:

1. **Researcher Node**
   - Searches Tavily for trending topics
   - Generates content ideas with AI
   - Validates research results

2. **Writer Node**
   - Crafts viral tweets (< 280 chars)
   - Adds hooks, emojis, and hashtags
   - Optimized for engagement

3. **Publisher Node** *(Optional in test mode)*
   - Posts tweet to X/Twitter
   - Returns confirmation

## ⚙️ Configuration

Edit `app/config.py` to customize:

- `LLM_MODEL`: AI model to use
- `LLM_TEMPERATURE_RESEARCH`: Temperature for research (0 = deterministic)
- `LLM_TEMPERATURE_CREATIVE`: Temperature for writing (0.7 = creative)
- `MAX_SEARCH_RESULTS`: Number of search results to analyze
- `MAX_TWEET_LENGTH`: Maximum tweet length

## 🧪 Testing

Test the bot without publishing:

```bash
uv run python test_bot.py
```

## 📝 Example Output

```
🧪 Testing AI Tweet Bot (No Publishing)...
📌 Niche: AI Agents in 2026

✅ Test completed!

📝 Content Idea:
Breaking: AI Agent 'Apex' achieves 38% profit surge...

🐦 Final Tweet:
🚨 BREAKING: AI 'Apex' just CRUSHED Q3 with a 38% profit surge! 
But the catch? 🤯 22% workforce reduction. 
Is this peak innovation or disaster? Your take! 👇 
#AIAgents #FutureOfWork #AIethics

📊 Tweet Length: 208 characters
```

## 🛡️ Error Handling

- Research validation ensures quality content
- Graceful error messages
- Test mode for safe development
- SSL error handling for Windows

## 📦 Dependencies

- `langchain` - LLM framework
- `langgraph` - Workflow orchestration
- `langchain-google-genai` - Google Gemini integration
- `langchain-community` - Tavily search
- `tweepy` - X/Twitter API
- `python-dotenv` - Environment management

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

MIT License

---

Made with ❤️ using LangGraph and AI
