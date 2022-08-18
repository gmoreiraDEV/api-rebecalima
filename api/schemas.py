from pydantic import BaseModel

class UserBase(BaseModel):
    name:str
    email:str
    password:str

class User(UserBase):
    class Config:
        orm_mode: True

class IngredientBase(BaseModel):
    name: str
    item: str

class Ingredient(IngredientBase):
    class Config:
        orm_mode: True

class MethodBase(BaseModel):
    name: str
    item: str

class Method(MethodBase):
    class Config:
        orm_mode: True

class RecipeBase(BaseModel):
    name: str
    notes: str
    time: str
    serving: str
    ingredients: list[Ingredient] = []
    methods: list[Method] = []

class Recipe(RecipeBase):
    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    recipes : list[Recipe] =[]
    
    class Config:
        orm_mode = True