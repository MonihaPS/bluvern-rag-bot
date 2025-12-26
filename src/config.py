import os
from dotenv import load_dotenv
# CHANGE IMPORT: Use the Inference API (Cloud) instead of local
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings 

load_dotenv()

# Page Settings
PAGE_TITLE = "Bluvern Intelligent Agent"
PAGE_ICON = "⚡"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN") 

# AI Settings
MODEL_NAME = "llama-3.3-70b-versatile"

# CHANGE THIS SECTION:
# Old (Heavy): EMBEDDING_MODEL = HuggingFaceEmbeddings(...)
# New (Light):
EMBEDDING_MODEL = HuggingFaceInferenceAPIEmbeddings(
    api_key=HUGGINGFACEHUB_API_TOKEN,
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

VECTOR_DB_DIR = "chroma_db_store"

# Data Processing
CHUNK_SIZE = 800
CHUNK_OVERLAP = 100