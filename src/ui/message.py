import streamlit as st


class Message:
    """
    Renders chat messages in a consistent format.

    Supports:
    - User messages
    - Assistant messages
    - Markdown rendering
    - Source citations
    - Response timing
    """

    @staticmethod
    def user(content: str):
        """
        Render user message.
        """

        with st.chat_message("user"):
            st.markdown(content)

    @staticmethod
    def assistant(
        content: str,
        sources=None,
        response_time=None,
    ):
        """
        Render assistant message.
        """

        with st.chat_message("assistant"):

            # -------------------------
            # Answer
            # -------------------------

            st.markdown(content)

            # -------------------------
            # Sources
            # -------------------------

            if sources:

                with st.expander("📄 Sources Used", expanded=False):

                    for index, doc in enumerate(sources, start=1):

                        metadata = doc.metadata

                        source = metadata.get(
                            "source",
                            "Unknown"
                        )

                        page = metadata.get(
                            "page",
                            "-"
                        )

                        chunk = metadata.get(
                            "chunk",
                            "-"
                        )

                        st.markdown(
                            f"""
**{index}. {source}**

- Page : {page}
- Chunk : {chunk}
"""
                        )

                        with st.expander(
                            "View Retrieved Text",
                            expanded=False,
                        ):
                            st.write(doc.page_content)

            # -------------------------
            # Statistics
            # -------------------------

            if response_time is not None:

                st.caption(
                    f"⏱ Response generated in "
                    f"{response_time:.2f} sec"
                )