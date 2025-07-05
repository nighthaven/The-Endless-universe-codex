from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    session_id: str
    selected_game: Optional[str] = None  # <- correct
    message: Optional[str] = None
