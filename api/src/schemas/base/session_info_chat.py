from typing import Any, List, Optional

from pydantic import BaseModel, Field


class SessionInfoChat(BaseModel):
    exists: bool = Field(..., description="Indique si la session existe")
    state: Optional[str] = Field(None, description="État de la conversation")
    selected_game: Optional[str] = Field(None, description="Jeu sélectionné")
    history_length: Optional[int] = Field(
        None, description="Nombre de messages dans l'historique"
    )
    last_messages: Optional[List[Any]] = Field(None, description="Derniers messages")
    message: Optional[str] = Field(None, description="Message informatif")

    class Config:
        json_schema_extra = {
            "example": {
                "exists": True,
                "state": "universe_ready",
                "selected_game": "Endless Space",
                "history_length": 8,
                "last_messages": [
                    {"user": "Endless Space"},
                    {"bot": "Parfait ! J'ai compris..."},
                ],
            }
        }
