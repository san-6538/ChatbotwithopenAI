from fastapi import FastAPI
from pydantic import BaseModel
from medical_rag import get_user_chain

app = FastAPI(title="Seva Medical RAG Chatbot (PDF)")

class Query(BaseModel):
    user_id: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    sources: list

@app.post("/ask", response_model=AnswerResponse)
def ask_medical(query: Query):
    chain = get_user_chain(query.user_id)
    result = chain({"question": query.question})
    sources = [doc.page_content[:200] for doc in result['source_documents']]
    return {"answer": result['answer'], "sources": sources}

@app.get("/")
def root():
    return {"message": "Seva Medical RAG Chatbot Backend (PDF) is running."}
