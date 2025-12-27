# Bluvern RAG Bot 🤖

A Retrieval-Augmented Generation (RAG) chatbot built for **Bluvern** to answer company-specific queries accurately using a private knowledge base.

---

## 🚀 Project Overview

This chatbot is designed to act as **Bluvern’s intelligent assistant**, answering questions related to:
- Company overview
- Services
- Careers
- Contact information
- General business queries

The system uses **Retrieval-Augmented Generation (RAG)** to ensure responses are grounded strictly in Bluvern’s internal knowledge, avoiding hallucinations.

---

## 🧠 Architecture

1. Company knowledge is stored in a structured text file.
2. The content is split into meaningful chunks.
3. Chunks are converted into vector embeddings.
4. A vector database retrieves the most relevant content.
5. A large language model generates answers strictly from retrieved data.

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **LangChain**
- **ChromaDB**
- **Groq LLM**
- **HTML/CSS (UI Demo)**

---

## 📂 Project Structure

src/
├── loader.py # Loads and splits knowledge base
├── vector_db.py # Vector store creation
├── model.py # RAG pipeline
├── server.py # FastAPI backend
├── config.py # Configuration settings
├── knowledge_base.txt


---

## 🔐 Security

- API keys are stored securely using environment variables.
- `.env` files are excluded from version control.
- No sensitive credentials are committed to GitHub.

---

## ▶️ Running the Project

```bash
pip install -r requirements.txt
python -m src.server

Open browser:
http://localhost:8000

👤 Author

Moniha P S
B.Tech Artificial Intelligence & Data Science

