from sqlalchemy.orm import Session

from app.models.medical_report import MedicalReport


def create_medical_report(
    db: Session,
    user_id: int,
    file_name: str,
    file_path: str,
):
    report = MedicalReport(
        user_id=user_id,
        file_name=file_name,
        file_path=file_path,
    )

    db.add(report)
    db.commit()
    db.refresh(report)

    return report