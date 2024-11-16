from pydantic import BaseModel


class PlanetResponse(BaseModel):
    id: int
    name: str
    type: str
    description: str

    class Config:
        from_attributes = True
