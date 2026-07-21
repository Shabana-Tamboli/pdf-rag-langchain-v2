import streamlit as st


class ChatWindow:
    """
    Renders the chat interface and interacts with the RAG service.
    """

    def __init__(self, rag_service):
        self.rag = rag_service

        if "messages" not in st.session_state:
            st.session_state.messages = []

    # ---------------------------------------------------------
    # Render Chat Window
    # ---------------------------------------------------------

    def render(self):

        st.title("🤖 QA AI Assistant")

        # ---------------------------------------------
        # Display Previous Conversation
        # ---------------------------------------------

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

                if (
                    message["role"] == "assistant"
                    and message.get("sources")
                ):

                    with st.expander("📄 Sources Used"):

                        for i, doc in enumerate(
                            message["sources"],
                            start=1,
                        ):

                            source = doc.metadata.get(
                                "source",
                                "Unknown"
                            )

                            page = doc.metadata.get(
                                "page",
                                "-"
                            )

                            st.markdown(
                                f"**{i}. {source}**"
                            )

                            st.write(f"Page : {page}")

                            with st.expander(
                                "Retrieved Text",
                                expanded=False,
                            ):
                                st.write(doc.page_content)

                if (
                    message["role"] == "assistant"
                    and message.get("time") is not None
                ):
                    st.caption(
                        f"⏱ Response Time : "
                        f"{message['time']:.2f} sec"
                    )

        # ---------------------------------------------
        # User Input
        # ---------------------------------------------

        question = st.chat_input(
            "Ask anything about your documents..."
        )

        if not question:
            return

        # ---------------------------------------------
        # Store & Show User Message
        # ---------------------------------------------

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        # ---------------------------------------------
        # Assistant Response
        # ---------------------------------------------

        with st.chat_message("assistant"):

            placeholder = st.empty()

            with st.spinner("Thinking..."):

                result = self.rag.ask(question)

            answer = ""

            # Simulated streaming effect
            for word in result["answer"].split():

                answer += word + " "

                placeholder.markdown(answer + "▌")

            placeholder.markdown(answer)

            docs = result["documents"]

            if docs:

                with st.expander("📄 Sources Used"):

                    for i, doc in enumerate(
                        docs,
                        start=1,
                    ):

                        source = doc.metadata.get(
                            "source",
                            "Unknown"
                        )

                        page = doc.metadata.get(
                            "page",
                            "-"
                        )

                        st.markdown(
                            f"**{i}. {source}**"
                        )

                        st.write(f"Page : {page}")

                        with st.expander(
                            "Retrieved Text",
                            expanded=False,
                        ):
                            st.write(doc.page_content)

            st.caption(
                f"⏱ Response Time : "
                f"{result['total_time']:.2f} sec"
            )

        # ---------------------------------------------
        # Save Assistant Message
        # ---------------------------------------------

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
                "sources": docs,
                "time": result["total_time"],
            }
        )