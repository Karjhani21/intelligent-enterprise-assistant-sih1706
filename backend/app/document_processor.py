from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    return "".join(page.extract_text() or "" for page in reader.pages)

def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join(p.text for p in doc.paragraphs)

def summarize_text(text: str, max_sentences: int = 3) -> str:
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    return '. '.join(sentences[:max_sentences]) + ('.' if sentences else '')

def extract_keywords(text: str, limit: int = 10):
    words = [w.strip('.,!?()[]{}').lower() for w in text.split()]
    words = [w for w in words if len(w) > 4]
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:limit]]
