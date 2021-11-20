from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from blog import database
from sqlalchemy.orm import Session
from blog.repository import authentication


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return authentication.login(request, db)
