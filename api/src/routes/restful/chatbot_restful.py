from fastapi import APIRouter, HTTPException
from src.schemas.base.chatbot_base import ChatRequest
from src.schemas.base.session_info_chat import SessionInfoChat
from src.schemas.response.chat_response import ChatResponse
from src.services.chatbot_service import ChatbotService

router = APIRouter(
    prefix="/endless/chatbot",
    tags=["chatbot"],
)

chatbot_service = ChatbotService()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    try:
        result = chatbot_service.process_chat_message(
            session_id=request.session_id,
            message=request.message,
            selected_game=request.selected_game,
        )

        return ChatResponse(
            response=result["response"],
            state=result["state"],
            selected_game=result["selected_game"],
        )

    except Exception as e:
        print(f"Erreur dans chat_endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur interne du serveur")


@router.post("/reset")
def reset_session_endpoint(request: ChatRequest):
    try:
        result = chatbot_service.reset_session(request.session_id)
        return result

    except Exception as e:
        print(f"Erreur dans reset_session: {str(e)}")
        raise HTTPException(
            status_code=500, detail="Erreur lors de la réinitialisation"
        )


@router.get("/session/{session_id}", response_model=SessionInfoChat)
def get_session_info_endpoint(session_id: str):
    try:
        result = chatbot_service.get_session_info(session_id)
        return SessionInfoChat(**result)

    except Exception as e:
        print(f"Erreur dans get_session_info: {str(e)}")
        raise HTTPException(
            status_code=500, detail="Erreur lors de la récupération de la session"
        )


@router.get("/health")
def health_check_endpoint():
    try:
        return chatbot_service.get_health_status()

    except Exception as e:
        print(f"Erreur dans health_check: {str(e)}")
        raise HTTPException(
            status_code=500, detail="Erreur lors de la vérification de santé"
        )
