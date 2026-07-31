from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message


def create_message(
    db: Session,
    conversation: Conversation,
    role: str,
    content: str,
) -> Message:

    message = Message(
        conversation_id=conversation.id,
        role=role,
        content=content,
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    return message

def get_conversation_messages(
    db: Session,
    conversation: Conversation,
):
    return (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation.id
        )
        .order_by(Message.created_at)
        .all()
    )