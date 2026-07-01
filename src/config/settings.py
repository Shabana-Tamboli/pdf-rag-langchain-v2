from pathlib import Path

# ==========================================
# Project Root
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ==========================================
# Directories
# ==========================================

DATA_DIR = BASE_DIR / "data"

UPLOAD_DIR = BASE_DIR / "uploads"

VECTOR_DB_DIR = BASE_DIR / "vector_db"

LOG_DIR = BASE_DIR / "logs"

# ==========================================
# Embedding Model
# ==========================================

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================
# Ollama Model
# ==========================================

OLLAMA_MODEL = "llama3"

# ==========================================
# Text Splitter
# ==========================================

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# ==========================================
# Retriever
# ==========================================

TOP_K_RESULTS = 5

# ==========================================
# Streamlit
# ==========================================

PAGE_TITLE = "QA AI Assistant"

PAGE_ICON = "🤖"

# ==========================================
# Supported Files
# ==========================================

SUPPORTED_FILES = [".pdf"]