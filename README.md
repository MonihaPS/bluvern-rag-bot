# Bluvern RAG Assistant

A local AI assistant that answers questions about Bluvern services using Retrieval-Augmented Generation (RAG).

## Features
- **Privacy First:** Runs entirely offline using local LLMs.
- **Zero Cost:** Uses open-source models (Llama 3.2 via Ollama).
- **Custom Knowledge:** Scrapes `bluvern.com` for real-time context.

## Setup Instructions

1. **Install Ollama**
   Download from [ollama.com](https://ollama.com) and pull the model:
   ```bash
   ollama pull llama3.2:1b