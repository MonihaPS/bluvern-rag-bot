# Bluvern RAG Bot 🤖

A Retrieval-Augmented Generation (RAG) chatbot built for **Bluvern** to answer company-specific queries accurately using a private knowledge base.

---

## 🚀 Project Overview

The Bluvern RAG Bot is designed to act as an intelligent assistant for Bluvern.  
It answers queries related to the company by retrieving verified information from a curated knowledge base and generating responses grounded strictly in that data.

The focus of this project is reliability, correctness, and production readiness.

---

## 🧠 Architecture

The system follows a standard Retrieval-Augmented Generation (RAG) workflow:

1. Company information is stored in a structured text-based knowledge file.
2. The content is split into meaningful chunks.
3. Each chunk is converted into vector embeddings.
4. A vector database retrieves the most relevant chunks for a user query.
5. A large language model generates answers strictly using the retrieved context.

This design avoids hallucinations and ensures company-aligned responses.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- Groq LLM
- HTML / CSS (demo interface)

---

## 📂 Project Structure

```text
src/
├── loader.py          # Loads and splits the knowledge base
├── vector_db.py       # Vector store creation (ChromaDB)
├── model.py           # RAG pipeline logic
├── server.py          # FastAPI backend
├── config.py          # Configuration settings
└── knowledge_base.txt # Bluvern company knowledge
```

---

## 🔐 Security

```yaml
security:
  api_keys:
    storage: environment_variables
    committed_to_repo: false
  env_file:
    name: .env
    tracked_in_git: false
  credentials:
    sensitive_data_in_repo: false
```

---

## 🔑 Environment Variables Setup

This project requires external API keys to run.

**API keys are not included in the repository** for security reasons and must be provided locally using environment variables.

**1. Create a `.env` file (local only)** inside the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Note:** The `.env` file is excluded from version control and should never be pushed to GitHub.

---

## ▶️ Running the Project

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Start the server**
```bash
python -m src.server
```

**3. Access the application**
Open your browser and go to:
[http://localhost:8000](http://localhost:8000)


---

## 👤 Author

**Moniha P S**<br>
B.Tech Artificial Intelligence & Data Science<br>
SREC
