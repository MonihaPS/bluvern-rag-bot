import os
from langchain_huggingface import HuggingFaceEmbeddings

# Page Settings
PAGE_TITLE = "Bluvern Intelligent Agent"
PAGE_ICON = "⚡"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# AI Settings (Speed Optimized)
MODEL_NAME = "llama-3.1-8b-instant"      # Fast model
EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # Fast embeddings
VECTOR_DB_DIR = "chroma_db_store"

# Data Processing
CHUNK_SIZE = 800  # Smaller chunks = less reading for AI = Faster Speed
CHUNK_OVERLAP = 100
SEARCH_K = 2     # Read only top 2 results (Speed Hack)

# Target
URL = "https://bluvern.com/"