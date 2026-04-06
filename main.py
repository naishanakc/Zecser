from fastapi import FastAPI


app = FastAPI(title="Zecpath AI")

@app.get("/")
def home():
    return {"message":"Zecpath AI Running Sucessfully"}

@app.get("/health")
def health():
    return {"status": "OK"}


from parsers.resume_parser.extractor import extract_folder

extract_folder("data/raw_resumes", "data/cleaned_resume")

print("All resumes processed successfully!")

def extract_skills(text):
    skills = [
        "mri", "ct scan", "x-ray", "ultrasound",
        "radiology", "pacs", "dicom", "diagnosis"
    ]

    found = []
    for skill in skills:
        if skill in text.lower():
            found.append(skill)

    return found


def calculate_score(resume_skills, jd_skills):
    if len(jd_skills) == 0:
        return 0

    match = set(resume_skills) & set(jd_skills)
    score = (len(match) / len(jd_skills)) * 100

    return round(score, 2)


# 