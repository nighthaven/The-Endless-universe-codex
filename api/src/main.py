from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.models.users_models import User
from src.routes.anomalies_routes import router as anomalies_router
from src.routes.auth_route import router as login_router
from src.routes.factions_routes import router as factions_router
from src.routes.media_routes import router as media_router
from src.routes.users_routes import router as user_router
from src.routes.wonders_routes import router as wonders_router
from src.utils.Oauth2 import get_current_user


app = FastAPI(
    title="The Endless Universe API",
    description="An API about the univers of Endless, by Amplitude Studio",
    version="1.0.0",
    openapi_tags=[
        {"name": "factions", "description": "Operations on factions"},
        {"name": "Anomalies", "description": "Operations on anomalies"},
        {"name": "Wonders", "description": "Operations on wonders"},
    ],
)


app.include_router(user_router)
app.include_router(login_router)
app.include_router(media_router)
app.include_router(anomalies_router)
app.include_router(wonders_router)
app.include_router(factions_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/testauth")
def read_testauth(current_user: User = Depends(get_current_user)):
    return {"authentifié": "Cette route montre que l'utilisateur est bien authentifié"}
