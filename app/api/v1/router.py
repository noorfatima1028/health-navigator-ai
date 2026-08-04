from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.conversation import router as conversation_router
from app.api.v1.message import router as message_router
from app.api.v1.symptom_assessment import router as symptom_assessment_router
router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Health Navigator AI",
    }


router.include_router(auth_router)
router.include_router(conversation_router)
router.include_router(message_router)
router.include_router(symptom_assessment_router)