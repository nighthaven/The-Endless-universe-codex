from typing import Optional

from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    """Schéma de réponse du chatbot"""

    response: str = Field(..., description="Réponse du chatbot")
    state: Optional[str] = Field(None, description="État actuel de la conversation")
    selected_game: Optional[str] = Field(
        None, description="Jeu actuellement sélectionné"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "response": "Parfait ! J'ai compris que tu veux parler d'Endless Space.",
                "state": "universe_ready",
                "selected_game": "Endless Space",
            }
        }
