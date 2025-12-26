import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src import config

def load_and_split_data(url):
    """Fetches, cleans, and chunks the website content."""
    print(f"🔄 Scraper: Fetching {url}...")
    
    try:
        # 1. Fetch
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        if response.status_code != 200:
            return None
        
        # 2. Clean
        soup = BeautifulSoup(response.content, 'html.parser')
        # Remove scripts and styles to reduce noise
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text(separator="\n")
        clean_lines = [line.strip() for line in text.splitlines() if line.strip()]
        clean_text = "\n".join(clean_lines)
        
        # 3. Create Document
        docs = [Document(page_content=clean_text, metadata={"source": url})]
        
        # 4. Split (Optimize chunk size for speed)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP
        )
        return splitter.split_documents(docs)
        
    except Exception as e:
        print(f"❌ Scraper Error: {e}")
        return None