from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI


class LLMClient:

    def __init__(self, provider, api_key, model):
        self.provider = provider

        if provider == "openai":
            self.llm = ChatOpenAI(model=model, api_key=api_key)
        elif provider == "anthropic":
            self.llm = ChatAnthropic(model=model, api_key=api_key)
        elif provider == "google":
            self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key)

    def bind_tools(self, tools):
        self.llm_with_tools = self.llm.bind_tools(tools)

    def invoke(self, messages):
        return self.llm_with_tools.invoke(messages)
