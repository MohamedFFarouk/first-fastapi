from fastapi import Response, status, HTTPException, Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import Token
from app.utils import verify
from ..database import get_db
from app.oauth2 import creat_access_token

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    user = db.query(User).filter(User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials"
        )
    access_token = creat_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
