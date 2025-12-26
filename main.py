import sys
import requests
from bs4 import BeautifulSoup

# Import LangChain components
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document

# --- Configuration ---
TARGET_URL = "https://bluvern.com/"
MODEL_NAME = "llama3.2:1b"  # Using 1B for faster inference on laptops
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def load_website(url):
    """Scrapes the target website and returns a Document object."""
    print(f"📥 Fetching content from {url}...")
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print(f"❌ Error: Failed to load page (Status: {response.status_code})")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator="\n")
        # Clean up whitespace
        clean_text = "\n".join([line.strip() for line in text.splitlines() if line.strip()])
        return [Document(page_content=clean_text, metadata={"source": url})]
    except Exception as e:
        print(f"❌ Error scraping website: {e}")
        return []

def main():
    # 1. Load Data
    docs = load_website(TARGET_URL)
    if not docs:
        print("No data found. Exiting.")
        sys.exit(1)

    # 2. Split Text
    print("⚙️  Processing content...")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 3. Create Vector Store
    print("🧠 Initializing knowledge base...")
    embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model)
    
    # Retrieve top 2 chunks to speed up processing
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    # 4. Initialize LLM
    print(f"🤖 Loading AI Model ({MODEL_NAME})...")
    llm = ChatOllama(model=MODEL_NAME, temperature=0)

    # 5. Create RAG Chain
    system_prompt = (
        "You are a professional assistant for Bluvern. "
        "Use the provided context to answer questions about Bluvern's services. "
        "If the answer is not in the context, say 'I do not have that information'."
        "\n\n"
        "Context: {context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    chain = create_retrieval_chain(retriever, create_stuff_documents_chain(llm, prompt))

    # 6. Chat Loop
    print("\n✅ Bluvern Assistant Ready! (Type 'quit' to exit)\n")
    while True:
        query = input("User: ")
        if query.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        
        print("Bot is thinking...", end="", flush=True)
        try:
            response = chain.invoke({"input": query})
            print(f"\rBot: {response['answer']}\n")
        except Exception as e:
            print(f"\r❌ Error: {e}\n")

if __name__ == "__main__":
    main()