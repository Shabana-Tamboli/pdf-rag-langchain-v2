import json
import streamlit as st

from src.config.settings import (
    OLLAMA_MODEL,
    EMBEDDING_MODEL,
)


class Sidebar:
    """
    Handles the application sidebar.

    Features
    --------
    ✓ Model Information
    ✓ Embedding Information
    ✓ Chat Statistics
    ✓ Export Chat
    ✓ Clear Conversation
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Render Sidebar
    # ---------------------------------------------------------

    def render(self):

        with st.sidebar:

            st.title("🤖 QA AI Assistant")

            st.divider()

            # -------------------------------------------------
            # Model Information
            # -------------------------------------------------

            st.subheader("🧠 Model")

            st.success(f"LLM : {OLLAMA_MODEL}")

            st.info(f"Embeddings : {EMBEDDING_MODEL}")

            st.divider()

            # -------------------------------------------------
            # Vector Store
            # -------------------------------------------------

            st.subheader("📚 Knowledge Base")

            st.write("FAISS Vector Database")

            st.success("Loaded Successfully")

            st.divider()

            # -------------------------------------------------
            # Conversation Statistics
            # -------------------------------------------------

            st.subheader("📊 Chat Statistics")

            total_messages = len(
                st.session_state.get("messages", [])
            )

            user_messages = len(
                [
                    m
                    for m in st.session_state.get("messages", [])
                    if m["role"] == "user"
                ]
            )

            assistant_messages = len(
                [
                    m
                    for m in st.session_state.get("messages", [])
                    if m["role"] == "assistant"
                ]
            )

            st.metric(
                "Total Messages",
                total_messages,
            )

            st.metric(
                "User Questions",
                user_messages,
            )

            st.metric(
                "AI Responses",
                assistant_messages,
            )

            st.divider()

            # -------------------------------------------------
            # Clear Chat
            # -------------------------------------------------

            st.subheader("🧹 Conversation")

            if st.button(
                "🗑 Clear Conversation",
                use_container_width=True,
            ):

                st.session_state.messages = []

                if "rag" in st.session_state:

                    st.session_state.rag.clear_memory()

                st.success("Conversation Cleared")

                st.rerun()

            st.divider()

            # -------------------------------------------------
            # Export Chat
            # -------------------------------------------------

            st.subheader("📥 Export Conversation")

            chat_json = json.dumps(
                st.session_state.get(
                    "messages",
                    [],
                ),
                indent=4,
                default=str,
            )

            st.download_button(
                label="⬇ Download JSON",
                data=chat_json,
                file_name="conversation.json",
                mime="application/json",
                use_container_width=True,
            )

            markdown = ""

            for msg in st.session_state.get("messages", []):

                role = (
                    "User"
                    if msg["role"] == "user"
                    else "Assistant"
                )

                markdown += f"## {role}\n\n"

                markdown += msg["content"]

                markdown += "\n\n"

            st.download_button(
                label="⬇ Download Markdown",
                data=markdown,
                file_name="conversation.md",
                mime="text/markdown",
                use_container_width=True,
            )

            st.divider()

            # -------------------------------------------------
            # About
            # -------------------------------------------------

            st.subheader("ℹ️ About")

            st.markdown(
                """
**Version:** Phase 3

**Framework:** LangChain

**Vector Store:** FAISS

**LLM:** Ollama

**UI:** Streamlit
"""
            )