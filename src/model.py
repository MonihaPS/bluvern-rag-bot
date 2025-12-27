from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src import config

def build_rag_chain(vectorstore):
    """Constructs the RAG pipeline using Groq Cloud LLM."""
    
    if not config.GROQ_API_KEY:
        raise ValueError("❌ Error: GROQ_API_KEY is missing in .env file")

    # 1. Groq LLM (Fast Cloud Brain)
    llm = ChatGroq(
        model=config.MODEL_NAME, 
        api_key=config.GROQ_API_KEY,
        temperature=0
    )
    
    # 2. Retriever (Local Vector Store)
    retriever = vectorstore.as_retriever(search_kwargs={"k": config.SEARCH_K})
    
    # 3. Prompt
    system_prompt = (
        "You are Bluvern's intelligent assistant. Your tone is professional and helpful. "
        "Answer the question based ONLY on the context below. "
        "If the answer is not in the context, say 'I don't have that info'.\n\n"
        "Context:\n{context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # 4. Chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    
    return rag_chain