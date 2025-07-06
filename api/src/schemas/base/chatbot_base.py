from typing import Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Schéma de requête pour le chatbot"""

    session_id: str = Field(..., description="Identifiant unique de la session")
    message: Optional[str] = Field(None, description="Message de l'utilisateur")
    selected_game: Optional[str] = Field(
        None, description="Jeu sélectionné par l'utilisateur"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "user123",
                "message": "Je veux parler d'Endless Space",
                "selected_game": None,
            }
        }
