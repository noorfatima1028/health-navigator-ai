from sqlalchemy.orm import Session

from app.auth.hashing import hash_password
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_data: UserCreate) -> User:
    hashed_password = hash_password(user_data.password)

    db_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=hashed_password,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user