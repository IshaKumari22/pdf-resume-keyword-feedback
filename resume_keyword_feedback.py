import fitz  # PyMuPDF
import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# 🔍 Required skills for a Data Analyst job
required_skills = {
    "excel", "sql", "python", "data analysis", "POWER BI",
    "tableau", "pandas", "numpy", "visualization", "statistics",
    "matplotlib", "reporting", "dashboard"
}

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def extract_keywords(text):
    # Lowercase and tokenize the full resume text
    lower_text = text.lower()
    found = set()

    for skill in required_skills:
        if skill.lower() in lower_text:
            found.add(skill)

    return found


def analyze_resume(resume_path):
    resume_text = extract_text_from_pdf(resume_path)
    found_skills = extract_keywords(resume_text)
    missing_skills = required_skills - found_skills

    print("✅ Found in Resume:", ", ".join(sorted(found_skills)))
    print("❌ Missing Skills:", ", ".join(sorted(missing_skills)) if missing_skills else "None – Great match!")

if __name__ == "__main__":
    resume_file = "Data_Analyst_Resume.pdf"  # Make sure this file is in the same folder
    analyze_resume(resume_file)
