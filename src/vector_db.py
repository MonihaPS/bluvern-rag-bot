from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from src import config

def setup_vectorstore(chunks):
    """Initializes the Vector DB with the chunks."""
    if not chunks:
        return None
        
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)
    
    # Create an in-memory vector store for speed
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings,
        collection_name="bluvern_data"
    )
    return vectorstore