import streamlit as st

from src.config.settings import (
    PAGE_TITLE,
    PAGE_ICON,
    VECTOR_DB_DIR,
)

from src.ui.styles import load_css
from src.ui.sidebar import Sidebar
from src.ui.chat_window import ChatWindow

from src.embeddings.embedding_manager import EmbeddingManager
from src.vector_store.vector_store_manager import VectorStoreManager
from src.services.rag_service import RAGService
from src.retriever.retriever import Retriever
from src.llm.ollama_client import OllamaClient

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
)

# ==========================================================
# Load Custom CSS
# ==========================================================

load_css()


# ==========================================================
# Cache Resource
# ==========================================================

@st.cache_resource(show_spinner="Loading QA AI Assistant...")
def load_rag():

    # -----------------------------------
    # Load Embeddings
    # -----------------------------------

    embedding_manager = EmbeddingManager()

    embeddings = embedding_manager.load_embeddings()

    # -----------------------------------
    # Load Vector Store
    # -----------------------------------

    vector_store = VectorStoreManager(
        VECTOR_DB_DIR,
        embeddings,
    )

    vector_store.load()

    # -----------------------------------
    # Create Retriever
    # -----------------------------------

    retriever = Retriever(vector_store)

    # -----------------------------------
    # Create Ollama Client
    # -----------------------------------

    llm_client = OllamaClient()

    # -----------------------------------
    # Create RAG Service
    # -----------------------------------

    rag = RAGService(
        retriever=retriever,
        llm_client=llm_client,
    )

    return rag

# ==========================================================
# Initialize Session State
# ==========================================================

if "rag" not in st.session_state:

    st.session_state.rag = load_rag()


# ==========================================================
# Sidebar
# ==========================================================

sidebar = Sidebar()

sidebar.render()


# ==========================================================
# Chat Window
# ==========================================================

chat = ChatWindow(
    st.session_state.rag
)

chat.render()