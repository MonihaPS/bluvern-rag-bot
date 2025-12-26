from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from src import config, loader, vector_db, model

# 1. Initialize the API
app = FastAPI()

# 2. Allow the website to talk to this backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any website (like bluvern.com) to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Global Variables for the Brain
rag_chain = None

class QueryRequest(BaseModel):
    query: str

@app.on_event("startup")
async def startup_event():
    """Load the model once when the server starts."""
    global rag_chain
    print("🚀 Server starting... Loading Knowledge Base...")
    chunks = loader.load_and_split_data(config.URL)
    store = vector_db.setup_vectorstore(chunks)
    rag_chain = model.build_rag_chain(store)
    print("✅ System Ready! API is listening.")

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    """The website sends a question here, we return the answer."""
    if not rag_chain:
        raise HTTPException(status_code=503, detail="System initializing...")
    
    # Run the RAG logic
    response = rag_chain.invoke({"input": request.query})
    
    return {
        "answer": response["answer"],
        # We send sources so the frontend can display them if needed
        "sources": [doc.page_content[:200] for doc in response["context"]]
    }
@app.get("/")
async def read_root():
    # This tells the server: "When someone visits the home URL, show them the HTML file"
    return FileResponse('demo_website.html')
# Run this file directly to start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)