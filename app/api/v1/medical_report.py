import os

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.medical_report import MedicalReportResponse
from app.services.medical_report import create_medical_report


router = APIRouter(
    prefix="/reports",
    tags=["Medical Reports"],
)


UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True,
)


@router.post(
    "/upload",
    response_model=MedicalReportResponse,
)
def upload_report(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    report = create_medical_report(
        db=db,
        user_id=current_user.id,
        file_name=file.filename,
        file_path=file_path,
    )

    return report