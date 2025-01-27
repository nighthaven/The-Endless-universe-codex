from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.routes.anomalies_routes import router as anomalies_router
from src.routes.auth_route import router as login_router
from src.routes.factions_routes import router as factions_router
from src.routes.media_routes import router as media_router
from src.routes.restful.all_url_restful import router as all_url_router
from src.routes.restful.anomalies_restful import router as anomalies_restful_router
from src.routes.restful.faction_description_restful import (
    router as faction_description_restful_router,
)
from src.routes.restful.factions_restful import router as factions_restful_router
from src.routes.restful.medias_restful import router as medias_restful_router
from src.routes.restful.planets_restful import router as planets_restful_router
from src.routes.restful.wonders_restful import router as wonders_restful_router
from src.routes.users_routes import router as user_router
from src.routes.wonders_routes import router as wonders_router

app = FastAPI(
    title="The Endless Universe API",
    description="An API about the univers of Endless, by Amplitude Studio",
    version="1.0.0",
    openapi_tags=[
        {"name": "endless", "description": "All URLs from the main object of the api"},
        {
            "name": "medias",
            "description": "Media are all existing medias, video game, books, etc... in the endless universe",
        },
        {
            "name": "anomalies",
            "description": "Anomalies are all existing anomalies on the endless universe",
        },
        {
            "name": "wonders",
            "description": "Wonders are all existing wonders on the endless universe",
        },
        {
            "name": "planets",
            "description": "Planets are all existing planets on the endless universe",
        },
        {
            "name": "factions",
            "description": "factions are all existing faction in the endless universe",
        },
        {
            "name": "faction-descriptions",
            "description": "Depending on the factions and media, the description of the faction will be displayed",
        },
    ],
)

routers = [
    user_router,
    login_router,
    media_router,
    anomalies_router,
    wonders_router,
    factions_router,
    anomalies_restful_router,
    all_url_router,
    medias_restful_router,
    wonders_restful_router,
    planets_restful_router,
    factions_restful_router,
    faction_description_restful_router,
]
for router in routers:
    app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/public", StaticFiles(directory="public"), name="public")
