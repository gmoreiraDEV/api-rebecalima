from functools import lru_cache
from fastapi import Depends, FastAPI
from api import models
from api.database import engine
from api.routers import user, recipe, authentication
from api.config import Settings

app = FastAPI()


@lru_cache()
def get_settings():
    return Settings()

models.Base.metadata.create_all(engine)

app.include_router(user.router)
app.include_router(recipe.router)
app.include_router(authentication.router)

@app.get('/info')
async def info(settings: Settings = Depends(get_settings)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user
    }
