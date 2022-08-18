from api import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from api.repository import user

router = APIRouter(prefix="/recipe", tags=["Recipes"])

get_db = database.get_db

@router.get('/')
def get_all_recipes():
    pass

@router.get('/{id}')
def get_one_recipe(id: str):
    pass

@router.post('/')
def create_recipe():
    pass

@router.put('/{id}')
def update_recipe(id: str):
    pass

@router.delete('/{id}')
def delete_recipe(id: str):
    pass