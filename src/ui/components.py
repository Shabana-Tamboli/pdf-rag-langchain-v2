import streamlit as st


# ==========================================================
# Success Message
# ==========================================================

def show_success(message: str):
    """
    Display success message.
    """
    st.success(message)


# ==========================================================
# Error Message
# ==========================================================

def show_error(message: str):
    """
    Display error message.
    """
    st.error(message)


# ==========================================================
# Warning Message
# ==========================================================

def show_warning(message: str):
    """
    Display warning message.
    """
    st.warning(message)


# ==========================================================
# Info Message
# ==========================================================

def show_info(message: str):
    """
    Display informational message.
    """
    st.info(message)


# ==========================================================
# Metrics
# ==========================================================

def render_metrics(response: dict):
    """
    Show Retrieval / Generation / Total Time.
    """

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🔍 Retrieval",
        f"{response['retrieval_time']:.2f} sec"
    )

    col2.metric(
        "🧠 Generation",
        f"{response['generation_time']:.2f} sec"
    )

    col3.metric(
        "⚡ Total",
        f"{response['total_time']:.2f} sec"
    )


# ==========================================================
# Sources
# ==========================================================

def render_sources(documents):
    """
    Display retrieved source documents.
    """

    if not documents:
        return

    with st.expander("📚 Retrieved Sources", expanded=False):

        for index, doc in enumerate(documents, start=1):

            st.markdown(f"### Document {index}")

            source = doc.metadata.get("source", "Unknown")

            page = doc.metadata.get("page", "-")

            st.write(f"**Source :** {source}")

            st.write(f"**Page :** {page}")

            st.write("---")

            st.write(doc.page_content)

            st.divider()


# ==========================================================
# Assistant Response
# ==========================================================

def render_answer(answer: str):
    """
    Display assistant answer.
    """

    st.markdown(answer)


# ==========================================================
# Thinking Animation
# ==========================================================

def thinking():
    """
    Placeholder spinner.
    """

    return st.spinner("🤖 Thinking...")


# ==========================================================
# Divider
# ==========================================================

def divider():
    st.divider()


# ==========================================================
# Empty State
# ==========================================================

def render_empty_chat():
    """
    Initial screen before first question.
    """

    st.markdown(
        """
# 👋 Welcome

Ask questions from your PDF knowledge base.

Example questions:

- What is Selenium?
- Explain Explicit Wait.
- Difference between Implicit and Fluent Wait.
- What is StaleElementReferenceException?
- Explain Page Object Model.
"""
    )