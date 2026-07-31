from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.message import MessageCreate, MessageResponse
from app.services.conversation import get_conversation_by_id
from app.services.message import (
    create_message,
    get_conversation_messages,
)

router = APIRouter(
    prefix="/conversations",
    tags=["Messages"],
)

@router.post(
    "/{conversation_id}/messages",
    response_model=MessageResponse,
)
def create_new_message(
    conversation_id: int,
    message: MessageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    conversation = get_conversation_by_id(
        db,
        conversation_id,
    )

    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        )

    if conversation.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied.",
        )

    return create_message(
        db=db,
        conversation=conversation,
        role="user",
        content=message.content,
    )

@router.get(
    "/{conversation_id}/messages",
    response_model=list[MessageResponse],
)
def list_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    conversation = get_conversation_by_id(
        db,
        conversation_id,
    )

    if conversation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conversation not found.",
        )

    if conversation.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied.",
        )

    return get_conversation_messages(
        db,
        conversation,
    )