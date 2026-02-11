from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Zecpath AI")
app.include_router(router)

@app.get("/")
def home():
    return {"message":"Zecpath AI Running Sucessfully"}

@app.get("/health")
def health():
    return {"status": "OK"}


