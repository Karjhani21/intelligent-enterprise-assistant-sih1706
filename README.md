# Intelligent Enterprise Assistant (SIH1706)

AI-powered enterprise chatbot developed for Smart India Hackathon (SIH) to improve organizational efficiency through NLP and deep learning techniques.

---

# 📌 Problem Statement

### Problem ID:
SIH1706

### Problem Title:
**Intelligent Enterprise Assistant: Enhancing Organizational Efficiency through AI-driven Chatbot Integration**

---

# 🚀 Project Overview

The Intelligent Enterprise Assistant is an AI-powered chatbot designed for large public sector organizations. The system helps employees quickly access HR policies, IT support information, company event details, and organizational resources.

The chatbot also includes document processing capabilities such as:
- Document summarization
- Keyword extraction
- Text extraction from uploaded documents

The system is designed to:
- Handle multiple users simultaneously
- Provide responses within 5 seconds
- Support OTP-based authentication
- Filter inappropriate language

---

# ✨ Features

## 🤖 AI Chatbot
- HR policy assistance
- IT support guidance
- Company event information
- Organizational FAQ support

## 📄 Document Processing
- PDF text extraction
- DOCX text extraction
- Document summarization
- Keyword extraction

## 🔐 Security
- Email OTP based 2FA authentication
- Secure API endpoints

## 🚫 Profanity Filter
- Detects and blocks inappropriate language using a system dictionary

## ⚡ Performance
- Fast API response
- Scalable architecture for parallel users

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API Framework |
| React | Frontend UI |
| Vite | Frontend Build Tool |
| NLP | Chatbot Processing |
| PyPDF2 | PDF Processing |
| python-docx | DOCX Processing |
| GitHub | Version Control |

---

# 📁 Project Structure

```text
enterprise-assistant/
│
├── backend/
│   ├── app/
│   │   ├── chatbot.py
│   │   ├── document_processor.py
│   │   ├── profanity.py
│   │   ├── database.py
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── main.jsx
│   │
│   └── package.json
│
├── data/
│   └── knowledge_base.json
│
├── screenshots/
│   ├── chatbot-home.png
│   ├── document-upload.png
│   ├── api-docs.png
│   └── otp-auth.png
│
└── README.md
```

---

# ⚙️ Installation & Setup

## 📌 Prerequisites

Install the following software:

- Python 3.10+
- Node.js
- Git
- VS Code (Recommended)

---

# 🔧 Backend Setup

Open terminal inside the backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend server:

```bash
python -m uvicorn app.main:app --reload
```

Backend will run at:

```text
http://localhost:8000
```

---

# 🎨 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the frontend:

```bash
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

# 📚 API Documentation

FastAPI Swagger documentation:

```text
http://localhost:8000/docs
```

---

# 🧪 Sample Queries

## HR Queries
- How many casual leaves do I have?
- What is maternity leave policy?
- Tell me about earned leave.

## IT Support Queries
- How do I reset my password?
- VPN connection issue
- Email login problem

## Event Queries
- When is the annual day?
- Upcoming company events

---

# 📄 Document Upload Features

Supported formats:
- PDF
- DOCX

Capabilities:
- Extract text
- Generate summaries
- Extract keywords

---

# 🚫 Profanity Filter Example

### Input:
```text
You are stupid
```

### Output:
```text
Please avoid using inappropriate language.
```

---

# 🔐 OTP Authentication

The chatbot supports:
- Email-based OTP verification
- Secure login validation

---

# 📷 Output Screenshots

## 🖥️ Chatbot Home Page
![Chatbot Home](screenshots/chatbot-home.png)

---

## 📄 Document Upload & Summary
![Document Upload](screenshots/document-upload.png)

---

## 📚 FastAPI Swagger Documentation
![API Docs](screenshots/api-docs.png)

---

## 🔐 OTP Authentication
![OTP Authentication](screenshots/otp-auth.png)

---

# 📈 Future Enhancements

- Voice-enabled chatbot
- Multi-language support
- Database integration
- AI-based semantic search
- Cloud deployment
- Mobile application support

---

# 🎯 Smart India Hackathon Objectives Achieved

✅ AI-based chatbot integration  
✅ NLP query understanding  
✅ Document analysis capability  
✅ OTP-based authentication  
✅ Profanity filtering  
✅ Scalable architecture  
✅ Fast response time  

# 🙏 Acknowledgements

- Smart India Hackathon
- FastAPI Documentation
- React Documentation
- Open Source Community

---

# ⭐ Conclusion

The Intelligent Enterprise Assistant improves organizational efficiency by providing employees with instant access to HR, IT, and organizational information using AI-powered conversational interfaces and document processing capabilities.

### Output

<img width="1877" height="673" alt="image" src="https://github.com/user-attachments/assets/00ce33f3-06c2-4573-9886-2c02343de3c7" />


