# 📄 PDF Resume Keyword Feedback Tool

This tool analyzes a resume PDF and checks whether it contains important skills based on a predefined job role or description. It helps candidates improve their resumes by identifying missing keywords.

## 🚀 Features

- Extracts text from PDF resumes using `PyMuPDF`
- Identifies key technical skills using `spaCy` NLP
- Prints:
  - ✅ Skills found
  - ❌ Skills missing

## 🧠 Technologies Used

- Python
- spaCy (`en_core_web_sm` language model)
- PyMuPDF (`fitz`)
- Virtual Environment (`venv`)

## 📂 File Structure

pdf_resume_keyword_feedback/
├── resume_keyword_feedback.py
├── your_resume.pdf
├── env/ (virtual environment)
└── README.md

## 📷 Sample Output Screenshot

![Output Screenshot](pdf_resume_keyword_output.png)

