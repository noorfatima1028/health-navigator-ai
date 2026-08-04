from pydantic import BaseModel


class SymptomAssessmentRequest(BaseModel):
    age: int
    sex: str
    symptoms: list[str]
    duration: str


class SymptomAssessmentResponse(BaseModel):
    assessment: str