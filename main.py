import sys
from src.config import load_config, run_setup
from src.llm_client import LLMClient
from src.agent import Agent


def main():
    config = load_config()
    if not config:
        config = run_setup()

    llm = LLMClient(config["provider"], config["api_key"], config["model"])
    agent = Agent(llm)

    print(f"\nAgent ready. Provider: {config['provider']}, Model: {config['model']}")
    print("Commands: 'quit' to exit, 'reset' to clear history, 'config' to reconfigure.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            break
        if user_input.lower() == "reset":
            agent.reset()
            print("Conversation history cleared.\n")
            continue
        if user_input.lower() == "config":
            config = run_setup(force=True)
            llm = LLMClient(config["provider"], config["api_key"], config["model"])
            agent = Agent(llm)
            print(f"\nReconfigured. Provider: {config['provider']}, Model: {config['model']}\n")
            continue

        try:
            response = agent.run(user_input)
            print(f"\nAgent: {response}\n")
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
