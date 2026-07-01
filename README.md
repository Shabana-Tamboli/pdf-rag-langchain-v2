git clone <repo>

cd pdf-rag-langchain-v2

python -m venv venv

# Windows
venv\Scripts\activate

pip install -e .

python -m src.ingest

streamlit run src/ui/app.py