# Your OpenClaw

A simple command-line AI agent inspired by OpenClaw. It uses a ReAct (Reason + Act) loop to autonomously call tools and answer questions. Supports multiple LLM providers.

## Supported Providers

| Provider | Default Model |
|----------|--------------|
| OpenAI | gpt-4o-mini |
| Anthropic | claude-sonnet-4-20250514 |
| Google Gemini | gemini-2.0-flash |

## Built-in Tools

- **read_file** - Read the contents of a file
- **write_file** - Write content to a file
- **list_directory** - List files and subdirectories
- **run_shell** - Execute a shell command

## Setup

```bash
python -m venv .venv

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

On launch, a menu is displayed:

```
🦞 Your OpenClaw

  1. Start Agent (CLI)
  2. Start Agent (Web)
  3. Configure
```

- **Option 1** — Starts the agent in the terminal (text chat)
- **Option 2** — Launches the Streamlit web interface in your browser
- **Option 3** — Configure LLM provider, model, and API key

### Configuration

Configuration is stored in your home directory, separate from the project:

```
~/.youropenclaw/
├── config.json    # LLM provider, model, and API key
└── skills/        # Skill files for heartbeat automation
```

This keeps API keys out of the project directory, reducing the risk of accidentally pushing sensitive data to GitHub.

### Web Interface

The web interface (option 2) provides:

- **Chat** — Full chatbot interface with message history
- **LLM Configuration** — Change provider, model, and API key from the sidebar
- **Skills Management** — Create, enable/disable, and delete skills
- **Heartbeat** — Start/stop a background loop that periodically runs enabled skills

### Skills

Skills are markdown files stored in `~/.youropenclaw/skills/`. Each skill defines an instruction that the agent executes on a schedule when the heartbeat is running.

```markdown
---
name: system-check
description: Check system health
schedule: 60
enabled: true
---

Check the system uptime and disk usage, then provide a brief summary.
```

### CLI Commands

| Command | Action |
|---------|--------|
| `quit` / `exit` | Exit the agent |
| `reset` | Clear conversation history |
| `config` | Reconfigure LLM provider and API key |

## Project Structure

```
your-openclaw/
  youropenclaw/
    web/
      app.py          - Streamlit web interface
    config.py         - Setup and configuration persistence
    llm_client.py     - Unified LLM client for all providers
    tools.py          - Tool definitions and execution logic
    agent.py          - ReAct agent loop
    skills.py         - Skills manager (create, toggle, delete)
    heartbeat.py      - Background heartbeat runner
  main.py             - Entry point
  requirements.txt    - Python dependencies
```

