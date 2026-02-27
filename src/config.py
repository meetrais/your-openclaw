import os
from pathlib import Path
from dotenv import load_dotenv, set_key


ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

PROVIDERS = {
    "1": "openai",
    "2": "anthropic",
    "3": "google",
}

DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "anthropic": "claude-sonnet-4-20250514",
    "google": "gemini-2.0-flash",
}


def load_config():
    load_dotenv(ENV_PATH)
    provider = os.getenv("LLM_PROVIDER")
    api_key = os.getenv("API_KEY")
    model = os.getenv("MODEL_NAME")
    if provider and api_key and model:
        return {"provider": provider, "api_key": api_key, "model": model}
    return None


def run_setup(force=False):
    existing = load_config()
    if existing and not force:
        return existing

    print("\n--- Agent Setup ---\n")
    print("Select LLM provider:")
    print("  1. OpenAI")
    print("  2. Anthropic")
    print("  3. Google Gemini")

    choice = ""
    while choice not in PROVIDERS:
        choice = input("\nEnter choice (1/2/3): ").strip()

    provider = PROVIDERS[choice]
    api_key = input("Enter API key: ").strip()

    default_model = DEFAULT_MODELS[provider]
    model_input = input(f"Enter model name [{default_model}]: ").strip()
    model = model_input if model_input else default_model

    ENV_PATH.touch(exist_ok=True)
    set_key(str(ENV_PATH), "LLM_PROVIDER", provider)
    set_key(str(ENV_PATH), "API_KEY", api_key)
    set_key(str(ENV_PATH), "MODEL_NAME", model)

    return {"provider": provider, "api_key": api_key, "model": model}
