import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .chatbot import get_response
from .profanity import contains_profanity
from .document_processor import (
    extract_text_from_pdf, extract_text_from_docx,
    summarize_text, extract_keywords
)

class QueryRequest(BaseModel):
    query: str

app = FastAPI(title="Enterprise Assistant API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Enterprise Assistant API is running"}

@app.post("/chat")
def chat(data: QueryRequest):
    if contains_profanity(data.query):
        return {"response": "Please avoid using inappropriate language."}
    return {"response": get_response(data.query)}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    ext = file.filename.lower().split(".")[-1]
    if ext == "pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == "docx":
        text = extract_text_from_docx(file_path)
    else:
        return {"error": "Only PDF and DOCX are supported"}

    return {
        "summary": summarize_text(text),
        "keywords": extract_keywords(text),
        "text_length": len(text)
    }
