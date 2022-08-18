import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    recipes = relationship('Recipe', back_populates="owner")

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    item = Column(String)
    recipe_id = Column(String, ForeignKey('recipes.id'))


class Method(Base):
    __tablename__ = 'methods'

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    item = Column(String)
    recipe_id = Column(String, ForeignKey('recipes.id'))

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    notes = Column(String)
    time = Column(String)
    serving = Column(String)
    user_id = Column(String, ForeignKey('users.id'))
    ingredients = relationship('Ingredient')
    methods = relationship('Method')
    owner = relationship('User', back_populates="recipes")
