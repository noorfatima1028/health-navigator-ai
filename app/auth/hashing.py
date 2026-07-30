from passlib.context import CryptContext

# Configure the password hashing context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Hash a plain text password.

    Args:
        password (str): The user's plain text password.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hashed version.

    Args:
        plain_password (str): Password entered by the user.
        hashed_password (str): Password stored in the database.

    Returns:
        bool: True if the password matches, otherwise False.
    """
    return pwd_context.verify(plain_password, hashed_password)