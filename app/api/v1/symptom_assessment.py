from fastapi import APIRouter

from app.schemas.symptom_assessment import (
    SymptomAssessmentRequest,
    SymptomAssessmentResponse,
)
from app.services.symptom_assessment import assess_symptoms

router = APIRouter(
    prefix="/symptom-assessment",
    tags=["Symptom Assessment"],
)


@router.post(
    "",
    response_model=SymptomAssessmentResponse,
)
def symptom_assessment(
    request: SymptomAssessmentRequest,
):
    response = assess_symptoms(
        age=request.age,
        sex=request.sex,
        symptoms=request.symptoms,
        duration=request.duration,
    )

    return SymptomAssessmentResponse(
        assessment=response,
    )