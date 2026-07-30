from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.conversation import (
    ConversationCreate,
    ConversationResponse,
)
from app.services.conversation import (
    create_conversation,
    get_user_conversations,
)

router = APIRouter(
    prefix="/conversations",
    tags=["Conversations"],
)

@router.post(
    "",
    response_model=ConversationResponse,
)
def create_new_conversation(
    conversation: ConversationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return create_conversation(
        db=db,
        title=conversation.title,
        user=current_user,
    )

@router.get(
    "",
    response_model=list[ConversationResponse],
)
def list_conversations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return get_user_conversations(
        db=db,
        user=current_user,
    )