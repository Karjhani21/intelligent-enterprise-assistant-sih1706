# intelligent-enterprise-assistant-sih1706
# Intelligent Enterprise Assistant (SIH1706)

AI-powered enterprise chatbot developed for Smart India Hackathon.

## Features
- HR policy query handling
- IT support assistance
- Company events information
- Document upload and summarization
- Keyword extraction
- Email OTP based 2FA
- Profanity filtering

## Technology Stack
- Backend: FastAPI
- Frontend: React
- NLP: Python
- Authentication: Email OTP
- Database: JSON / PostgreSQL (optional)

## Project Structure
enterprise-assistant/
├── backend/
├── frontend/
├── data/
└── README.md

## Sample Questions
- How many casual leaves do I have?
- How do I reset my password?
- When is the annual day?

## How to Run

### Backend
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
### Output

<img width="1877" height="673" alt="image" src="https://github.com/user-attachments/assets/00ce33f3-06c2-4573-9886-2c02343de3c7" />


