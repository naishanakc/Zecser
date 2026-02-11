from pydantic import BaseModel
class Candidate(BaseModel):
    experience: int
    skills:int