from fastapi import  HTTPException,Depends
from sqlmodel import Session,select
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.database import get_session
from app.auth import verify_token
from app.models.user_model import User

SessionDep = Annotated[Session,Depends(get_session)]
oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:Annotated[str,Depends(oauth_scheme)],session:SessionDep):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401,detail="Invalid token")
    user = session.exec(select(User).where(User.email==payload.get("sub"))).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user
