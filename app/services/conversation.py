from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.user import User


def create_conversation(
    db: Session,
    title: str,
    user: User,
) -> Conversation:

    conversation = Conversation(
        title=title,
        user_id=user.id,
    )

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation

def get_user_conversations(
    db: Session,
    user: User,
):
    return (
        db.query(Conversation)
        .filter(
            Conversation.user_id == user.id
        )
        .all()
    )