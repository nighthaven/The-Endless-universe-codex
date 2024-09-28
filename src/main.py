from typing import Union
from fastapi import FastAPI
from src.models import engine

app = FastAPI()

#test_model.Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}
