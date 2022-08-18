from unicodedata import name
from sqlalchemy.orm import Session
from api import models, schemas
from fastapi import HTTPException, status
from api.hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = models.User(name =request.name, email = request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session):
    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There are no registered users")
    return user
    
def get_one(id: str, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id} is not available")
    return user