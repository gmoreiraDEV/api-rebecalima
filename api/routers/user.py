from api import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from api.repository import user

router = APIRouter(prefix="/user", tags=["Users"])

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/', response_model=list[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return user.get_all(db)

@router.get('/{id}', response_model=schemas.ShowUser)
def get_one_user(id: str, db: Session = Depends(get_db)):
    return user.get_one(id, db)