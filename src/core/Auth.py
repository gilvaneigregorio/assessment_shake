from typing import Optional, MutableMapping, List, Union
from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
from jose import jwt, JWTError

from core.Database import get_db
from core.Security import verify_password
from models.dao.User import User
from models.dto.TokenData import TokenData
from repository import UserRepositoty


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"/v1/login")

# 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
ALGORITHM: str = "HS256"

async def authenticate(*, email: str, password: str, db: Session) -> Optional[User]:
    user = await UserRepositoty.get_one_by_email(db = db, email = email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def create_access_token(*, sub: str) -> str:
    return _create_token(
        token_type = "access_token",
        lifetime = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES),
        sub = sub,
    )


def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    payload["type"] = token_type
    payload["exp"] = expire
    payload["iat"] = datetime.utcnow()
    payload["sub"] = str(sub)
    return jwt.encode(payload, JWT_SECRET, algorithm = ALGORITHM)


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms = [ALGORITHM],
            options = {"verify_aud": False},
        )
        username: str = payload.get("sub")
    
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = UserRepositoty.get_one_by_id(db = db, id = token_data.username)
    if user is None:
        raise credentials_exception
    return user
