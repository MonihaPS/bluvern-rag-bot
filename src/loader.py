from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src import config
import os

def load_and_split_data(url=None):
    """
    Loads data from the local 'knowledge_base.txt' file 
    instead of scraping the internet.
    """
    # 1. Locate the file safely
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "knowledge_base.txt")
    
    print(f"📄 Loading Knowledge Base from: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Knowledge file not found at {file_path}")
        print("   Please create 'src/knowledge_base.txt' first!")
        return []

    try:
        # 2. Load the text file
        loader = TextLoader(file_path, encoding='utf-8')
        data = loader.load()
        
        # 3. Split into chunks (Paragraphs)
        # We use a slightly larger chunk size to keep context together
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=200
        )
        chunks = text_splitter.split_documents(data)
        
        print(f"✅ Loaded {len(chunks)} knowledge chunks.")
        return chunks
        
    except Exception as e:
        print(f"⚠️ Error processing knowledge base: {e}")
        return []