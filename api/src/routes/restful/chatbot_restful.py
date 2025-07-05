from typing import Any, Dict

from fastapi import APIRouter
from openai import OpenAI
from src.config import settings
from src.schemas.base.chatbot_base import ChatRequest

router = APIRouter(
    prefix="/endless/chatbot",
    tags=["chatbot"],
)

client = OpenAI(api_key=f"{settings.open_api_key}")

chat_sessions: Dict[str, Dict[str, Any]] = {}


@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    session = chat_sessions.get(
        request.session_id, {"selected_game": None, "history": []}
    )

    if session["selected_game"] is None:
        if request.selected_game is None:
            return {
                "response": "Bienvenue dans le Codex Endless ! Quel jeu choisis-tu ? (Endless Legend, Endless Space, Endless Space 2, etc.)"
            }
        else:
            session["selected_game"] = request.selected_game
            chat_sessions[request.session_id] = session
            return {
                "response": f"Tu as choisi {request.selected_game}. Pose-moi une question sur cet univers."
            }

    if request.message:
        if request.message.strip().lower() == "/end":
            chat_sessions.pop(request.session_id, None)
            return {"response": "Session terminée. À bientôt dans le Codex Endless !"}
        session["history"].append({"user": request.message})

        prompt = f"Dans le jeu {session['selected_game']}, réponds à la question suivante : {request.message}"

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
        except Exception as e:
            answer = f"Erreur de l'IA : {str(e)}"

        session["history"].append({"bot": answer})
        chat_sessions[request.session_id] = session
        return {"response": answer}

    return {"response": "Pose-moi une question sur le jeu sélectionné."}
