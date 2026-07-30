from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class SymptomAssessment(Base):
    __tablename__ = "symptom_assessments"

    id: Mapped[int] = mapped_column(primary_key=True)

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"),
        unique=True,
        nullable=False,
    )

    possible_conditions: Mapped[str] = mapped_column(Text)

    urgency_level: Mapped[str]

    recommendation: Mapped[str] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    conversation = relationship(
        "Conversation",
        back_populates="assessment",
    )