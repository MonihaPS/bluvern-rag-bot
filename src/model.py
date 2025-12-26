from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src import config

def build_rag_chain(vectorstore):
    """Constructs the RAG pipeline using Groq Cloud API."""
    
    # 1. Cloud LLM (Super Fast)
    if not config.GROQ_API_KEY:
        raise ValueError("❌ Error: Missing Groq API Key in config.py")

    llm = ChatGroq(
        model=config.MODEL_NAME, 
        api_key=config.GROQ_API_KEY,
        temperature=0
    )
    
    # 2. Retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": config.SEARCH_K})
    
    # 3. Professional Persona Prompt
    system_prompt = (
        "You are Bluvern's intelligent assistant. Your tone is professional, confident, and helpful. "
        "Answer the question DIRECTLY and CONCISELY. "
        "Do NOT use phrases like 'Based on the context' or 'The text says'. "
        "If the answer is not in the context, politely say: 'I do not have that specific information right now.'\n\n"
        "Context:\n{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # 4. Connect Chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain