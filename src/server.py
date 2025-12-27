import os
# DISABLE TELEMETRY TO PREVENT CRASHES
os.environ["ANONYMIZED_TELEMETRY"] = "False"
os.environ["SCARF_NO_ANALYTICS"] = "true"

import sys
# FIX IMPORT PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src import config, loader, vector_db, model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_chain = None

class QueryRequest(BaseModel):
    query: str

@app.on_event("startup")
async def startup_event():
    global rag_chain
    print("\n" + "="*50)
    print("🚀 BLUVERN AI (LOCAL BRAIN) IS STARTING...")
    print("="*50)
    
    try:
        chunks = loader.load_and_split_data(config.URL)
        store = vector_db.setup_vectorstore(chunks)
        if store:
            rag_chain = model.build_rag_chain(store)
            print("\n✅ SYSTEM READY!")
            print(f"👉 Go to: http://localhost:8000")
        else:
            print("❌ Failed to create brain. Check internet or URL.")
            
    except Exception as e:
        print(f"❌ Critical Error: {e}")

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    if not rag_chain:
        raise HTTPException(status_code=503, detail="System initializing...")
    
    response = rag_chain.invoke({"input": request.query})
    return {"answer": response["answer"]}

@app.get("/")
async def read_root():
    return FileResponse('demo_website.html')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)