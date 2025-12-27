from langchain_community.vectorstores import Chroma
from src import config
import shutil
import os

def setup_vectorstore(documents):
    if not documents:
        print("⚠️ No documents found to index.")
        return None

    # Optional: Clear old DB to prevent duplicates (Uncomment if needed)
    # if os.path.exists(config.VECTOR_DB_DIR):
    #     shutil.rmtree(config.VECTOR_DB_DIR)

    print(f"📦 Creating Local Vector Store for {len(documents)} chunks...")
    
    # Creates the DB locally using the CPU model
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=config.EMBEDDING_MODEL,
        persist_directory=config.VECTOR_DB_DIR
    )
    
    return vectorstore