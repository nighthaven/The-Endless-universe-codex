from typing import Union
from fastapi import FastAPI, Depends
from src.models import engine
from src.routes.users_routes import router as user_router
from src.routes.auth_route import router as login_router
from src.utils.Oauth2 import get_current_user
from src.models.users_models import User

app = FastAPI()

app.include_router(user_router)
app.include_router(login_router)

#test_model.Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/testauth")
def read_testauth(current_user: User = Depends(get_current_user)):
    return {"authentifié": "Cette route montre que l'utilisateur est bien authentifié"}