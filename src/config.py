import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings # Local Model

load_dotenv()

# Page Settings
PAGE_TITLE = "Bluvern Intelligent Agent"
PAGE_ICON = "⚡"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# AI Settings
MODEL_NAME = "llama-3.3-70b-versatile"
URL = "https://bluvern.com"

# --- LOCAL EMBEDDINGS (The "Large Brain") ---
# This runs on your CPU. It downloads the model once.
print("⚙️ Loading Local Embedding Model (This takes a moment)...")
EMBEDDING_MODEL = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

VECTOR_DB_DIR = "chroma_db_store"

# Data Processing
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
SEARCH_K = 3 # Number of sources to retrieve