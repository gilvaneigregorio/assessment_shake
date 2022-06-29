import fastapi
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any

from core.database import get_db, AsyncSession
from core.auth import authenticate, create_access_token
from models.dto.user import UserCreate, User as UserDTO
from repository import user_repositoty

router = fastapi.APIRouter(tags=["auth"])


@router.post("/login")
async def login(
    db: AsyncSession = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = await authenticate(
        email=form_data.username, password=form_data.password, db=db
    )
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )

    return {
        "access_token": create_access_token(sub=user.id),
        "token_type": "bearer",
    }


@router.post("/signup", response_model=UserDTO, status_code=201)
async def create_user_signup(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: UserCreate,
) -> Any:
    user = await user_repositoty.get_one_by_email(db=db, email=user_in.email)
    print(user_in.email)
    if user:
        raise HTTPException(
            status_code=400, detail="An user with this email already exists"
        )
    print(user)
    user = await user_repositoty.create(db=db, obj_in=user_in)

    return user
