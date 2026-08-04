from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth.hashing import verify_password
from app.auth.jwt import create_access_token
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.user import get_user_by_email


def authenticate_user(
    db: Session,
    credentials: LoginRequest,
) -> TokenResponse:

    user = get_user_by_email(
        db,
        credentials.email,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    if not verify_password(
        credentials.password,
        user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
        }
    )

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
    )