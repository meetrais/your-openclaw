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

On first run, the agent will prompt you to select an LLM provider, enter your API key, and choose a model. This configuration is saved to a `.env` file for subsequent runs.

### Interactive Commands

| Command | Action |
|---------|--------|
| `quit` / `exit` | Exit the agent |
| `reset` | Clear conversation history |
| `config` | Reconfigure LLM provider and API key |

## Project Structure

```
your-openclaw/
  src/
    config.py       - CLI setup and configuration persistence
    llm_client.py   - Unified LLM client for all providers
    tools.py        - Tool definitions and execution logic
    agent.py        - ReAct agent loop
  main.py           - Entry point
  requirements.txt  - Python dependencies
  .env.example      - Environment variable template
```
