# 📁 Project Structure

```
xAi-bot/
│
├── 📄 main.py                    # CLI entry point (interactive mode)
├── 📄 run_bot.py                 # Production runner (with publishing)
├── 📄 test_bot.py                # Test runner (without publishing)
├── 📄 README.md                  # Project documentation
├── 📄 pyproject.toml             # Dependencies and project config
├── 📄 .env                       # Environment variables (API keys)
├── 📄 .gitignore                 # Git ignore rules
└── 📄 uv.lock                    # Dependency lock file
│
└── 📁 app/                       # Main application package
    │
    ├── 📄 config.py              # Configuration & environment setup
    ├── 📄 models.py              # Data models (BotState TypedDict)
    ├── 📄 workflow.py            # LangGraph workflow definition
    ├── 📄 main.py                # App instances (app, app_test)
    │
    └── 📁 nodes/                 # LangGraph workflow nodes
        ├── 📄 __init__.py        # Node exports
        ├── 📄 researcher.py      # Research node (Tavily search + AI)
        ├── 📄 writer.py          # Tweet writer node (AI generation)
        └── 📄 publisher.py       # X/Twitter publisher node
```

## 🗂️ File Descriptions

### Root Level

- **`main.py`**: Interactive CLI for choosing test/live mode and entering niche
- **`run_bot.py`**: Direct runner for production (publishes to X/Twitter)
- **`test_bot.py`**: Safe testing without publishing to X
- **`README.md`**: Complete project documentation
- **`pyproject.toml`**: Python project configuration and dependencies
- **`.env`**: Environment variables (API keys - not in git)

### `app/` Package

Core application logic organized as a Python package.

- **`config.py`**: 
  - Loads environment variables
  - Defines constants (LLM settings, API configs)
  - Single source of truth for configuration

- **`models.py`**: 
  - `BotState` TypedDict definition
  - Data structures used throughout the workflow

- **`workflow.py`**: 
  - LangGraph workflow builder
  - Conditional edges and validation logic
  - Creates both `app` (with publisher) and `app_test` (without)

- **`main.py`**: 
  - Exports compiled workflow instances
  - `app` - production workflow
  - `app_test` - test workflow

### `app/nodes/` Package

Individual workflow nodes following single responsibility principle.

- **`researcher.py`**: 
  - Uses Tavily API to search for trending topics
  - AI analysis of search results
  - Error handling and validation

- **`writer.py`**: 
  - Generates viral tweets using Google Gemini
  - Applies tweet optimization guidelines
  - Ensures < 280 character limit

- **`publisher.py`**: 
  - Posts tweets to X/Twitter using Tweepy
  - Success/failure handling
  - Only used in production workflow

## 🔄 Workflow Flow

```
START
  ↓
[Researcher Node]
  ↓ (validate_research)
  ├─ fail → END
  └─ pass → [Writer Node]
              ↓
            [Publisher Node]* (optional)
              ↓
            END

* Publisher node only in production mode
```

## ✅ Clean Architecture Benefits

1. **Separation of Concerns**: Each file has a single, clear purpose
2. **Testability**: Easy to test nodes individually
3. **Maintainability**: Changes to one component don't affect others
4. **Scalability**: Easy to add new nodes or features
5. **Readability**: Clear structure for new developers
6. **Reusability**: Nodes can be reused in different workflows

## 🚀 Usage Examples

```bash
# Interactive mode
python main.py

# Test mode (no publishing)
python test_bot.py

# Production mode (with publishing)
python run_bot.py

# CLI with arguments
python main.py --test "Your Niche"
python main.py "Your Niche"
```

## 📦 Dependencies by Module

- **config.py**: `python-dotenv`
- **researcher.py**: `langchain-community`, `langchain-google-genai`, `tavily-python`
- **writer.py**: `langchain-google-genai`
- **publisher.py**: `tweepy`
- **workflow.py**: `langgraph`
