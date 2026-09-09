from pwdlib import PasswordHash
import jwt


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )


SECRET_KEY = "change-this-secret-key"
ALGORITHM = "HS256"


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token