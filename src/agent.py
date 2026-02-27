from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from src.tools import TOOL_DEFINITIONS, execute_tool


SYSTEM_PROMPT = """You are a helpful AI assistant with access to tools for interacting with the local file system and running shell commands. Use tools when the user's request requires reading files, writing files, listing directories, or executing commands. Provide clear, direct answers. When you use a tool, explain what you did and share the relevant results."""

MAX_ITERATIONS = 15


class Agent:

    def __init__(self, llm_client):
        self.llm = llm_client
        self.llm.bind_tools(TOOL_DEFINITIONS)
        self.messages = [SystemMessage(content=SYSTEM_PROMPT)]

    def reset(self):
        self.messages = [SystemMessage(content=SYSTEM_PROMPT)]

    def run(self, user_input):
        self.messages.append(HumanMessage(content=user_input))

        for _ in range(MAX_ITERATIONS):
            response = self.llm.invoke(self.messages)
            self.messages.append(response)

            if not response.tool_calls:
                return self._extract_text(response.content)


            for tc in response.tool_calls:
                result = execute_tool(tc["name"], tc["args"])
                self.messages.append(ToolMessage(
                    content=result,
                    tool_call_id=tc["id"],
                ))

        return "Reached maximum iterations. Please try a simpler request."

    @staticmethod
    def _extract_text(content):
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts = []
            for block in content:
                if isinstance(block, str):
                    parts.append(block)
                elif isinstance(block, dict) and "text" in block:
                    parts.append(block["text"])
            return "\n".join(parts)
        return str(content)

