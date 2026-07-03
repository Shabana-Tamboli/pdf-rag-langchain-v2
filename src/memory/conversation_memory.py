from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    BaseMessage,
)


class ConversationMemory:
    """
    Manages the conversation history between the user and the AI.

    Responsibilities:
    - Store user messages
    - Store AI responses
    - Return conversation history
    - Clear history
    """

    def __init__(self):

        self.messages: list[BaseMessage] = []

    # ---------------------------------------------------------
    # Add User Message
    # ---------------------------------------------------------

    def add_user_message(self, message: str):

        self.messages.append(
            HumanMessage(content=message)
        )

    # ---------------------------------------------------------
    # Add AI Message
    # ---------------------------------------------------------

    def add_ai_message(self, message: str):

        self.messages.append(
            AIMessage(content=message)
        )

    # ---------------------------------------------------------
    # Get Conversation History
    # ---------------------------------------------------------

    def get_messages(self):

        return self.messages

    # ---------------------------------------------------------
    # Get Last N Messages
    # ---------------------------------------------------------

    def get_last_messages(self, n: int = 10):

        return self.messages[-n:]

    # ---------------------------------------------------------
    # Total Messages
    # ---------------------------------------------------------

    def size(self):

        return len(self.messages)

    # ---------------------------------------------------------
    # Clear Memory
    # ---------------------------------------------------------

    def clear(self):

        self.messages.clear()

    # ---------------------------------------------------------
    # Is Empty
    # ---------------------------------------------------------

    def is_empty(self):

        return len(self.messages) == 0

    # ---------------------------------------------------------
    # Print Memory (Debugging)
    # ---------------------------------------------------------

    def print_memory(self):

        print("\n")
        print("=" * 80)
        print("CONVERSATION MEMORY")
        print("=" * 80)

        for msg in self.messages:

            role = (
                "User"
                if isinstance(msg, HumanMessage)
                else "Assistant"
            )

            print(f"\n{role}:")
            print(msg.content)