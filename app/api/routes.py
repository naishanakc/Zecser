from fastapi import APIRouter
from app.schemas.candidate import Candidate
from app.services.scoring import calculate_score

router = APIRouter()

@router.post("/predict")
def predict(candidate: Candidate):
    score = calculate_score(candidate.experience, candidate.skills)
    return {"score": score}