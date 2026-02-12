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