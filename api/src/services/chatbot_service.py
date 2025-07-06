from typing import Any, Dict, List, Optional, cast

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam
from src.config import settings
from src.enums.conversation_state import ConversationState


class ChatbotService:
    ENDLESS_UNIVERSES = [
        "endless space",
        "endless legend",
        "endless dungeon",
        "dungeon of the endless",
        "endless space 2" "endless legend 2",
    ]

    def __init__(self) -> None:
        self.client = OpenAI(api_key=f"{settings.open_api_key}")
        self.chat_sessions: Dict[str, Dict[str, Any]] = {}

    def is_valid_endless_universe(self, user_input: str) -> bool:
        if not user_input:
            return False

        input_lower = user_input.lower().strip()
        return any(universe in input_lower for universe in self.ENDLESS_UNIVERSES)

    def extract_endless_universe(self, user_input: str) -> Optional[str]:
        if not user_input:
            return None

        input_lower = user_input.lower().strip()
        for universe in self.ENDLESS_UNIVERSES:
            if universe in input_lower:
                return universe.title()
        return None

    def get_or_create_session(self, session_id: str) -> Dict[str, Any]:
        if session_id not in self.chat_sessions:
            self.chat_sessions[session_id] = {
                "selected_game": None,
                "history": [],
                "state": ConversationState.ASKING_UNIVERSE,
            }
        return self.chat_sessions[session_id]

    def build_system_context(self, selected_game: Optional[str]) -> str:
        if not selected_game:
            return "Tu es un assistant expert des univers Endless d'Amplitude Studios."

        base_context = f"""Tu es un assistant expert des univers Endless d'Amplitude Studios.

IMPORTANT: Tu te concentres EXCLUSIVEMENT sur l'univers {selected_game}. 
- NE réponds QUE sur {selected_game}
- Si on te demande quelque chose sur un autre jeu Endless, rappelle que tu te concentres sur {selected_game}
- Toutes tes réponses doivent concerner {selected_game} uniquement
- Si tu ne connais pas une information spécifique sur {selected_game}, dis-le clairement

Tu as accès à l'historique complet de la conversation pour maintenir le contexte sur {selected_game}."""

        return base_context

    def build_messages_for_openai(
        self, session: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        system_context = self.build_system_context(session.get("selected_game"))
        messages = [{"role": "system", "content": system_context}]

        for exchange in session["history"]:
            if "user" in exchange:
                messages.append({"role": "user", "content": exchange["user"]})
            if "bot" in exchange:
                messages.append({"role": "assistant", "content": exchange["bot"]})

        return messages

    def handle_universe_selection(
        self, session: Dict[str, Any], user_input: str
    ) -> str:
        if self.is_valid_endless_universe(user_input):
            selected_universe = self.extract_endless_universe(user_input)
            old_game = session.get("selected_game")

            session["selected_game"] = selected_universe
            session["state"] = ConversationState.UNIVERSE_READY

            if old_game and old_game != selected_universe:
                return f"""Parfait ! J'ai changé d'univers. Je me concentre maintenant sur {selected_universe}. 
J'ai oublié tout ce qui concernait {old_game}. 
Pose-moi tes questions sur {selected_universe} et je t'aiderai avec plaisir !"""
            else:
                return f"""Parfait ! J'ai compris que tu veux parler de {selected_universe}. 
Je me concentre exclusivement sur cet univers d'Amplitude Studios. 
Pose-moi tes questions sur {selected_universe} et je t'aiderai avec plaisir !"""
        else:
            return """Je ne reconnais pas cet univers. Je peux t'aider avec les univers Endless d'Amplitude Studios :
• Endless Space
• Endless Legend  
• Endless Dungeon
• Dungeon of the Endless
• Endless Space 2

Peux-tu me dire sur quel univers Endless tu veux que je t'aide ?"""

    def handle_universe_question(
        self, session: Dict[str, Any], user_message: str
    ) -> Optional[str]:
        try:
            messages = cast(
                List[ChatCompletionMessageParam],
                self.build_messages_for_openai(session),
            )

            messages.append({"role": "user", "content": user_message})

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"Erreur OpenAI: {str(e)}")
            return "Désolé, j'ai rencontré une erreur technique. Peux-tu reformuler ta question ?"

    def process_chat_message(
        self,
        session_id: str,
        message: Optional[str] = None,
        selected_game: Optional[str] = None,
    ) -> Dict[str, Any]:
        session = self.get_or_create_session(session_id)

        if message and message.strip().lower() == "/end":
            self.chat_sessions.pop(session_id, None)
            return {
                "response": "Session terminée. À bientôt dans le Codex Endless !",
                "state": None,
                "selected_game": None,
            }

        if session["state"] == ConversationState.ASKING_UNIVERSE:
            if not message and not selected_game:
                return {
                    "response": "Bienvenue dans le Codex Endless ! Sur quel univers Endless d'Amplitude Studios veux-tu que je t'aide ?",
                    "state": session["state"],
                    "selected_game": None,
                }

            universe_input = selected_game or message
            if universe_input:
                response_text = self.handle_universe_selection(session, universe_input)

                session["history"].append({"user": universe_input})
                session["history"].append({"bot": response_text})

                return {
                    "response": response_text,
                    "state": session["state"],
                    "selected_game": session.get("selected_game"),
                }

        elif session["state"] == ConversationState.UNIVERSE_READY:
            if message and self.is_valid_endless_universe(message):
                old_game = session.get("selected_game")
                new_universe = self.extract_endless_universe(message)

                if old_game != new_universe:
                    session["history"] = []

                response_text = self.handle_universe_selection(session, message)

                session["history"].append({"user": message})
                session["history"].append({"bot": response_text})

                return {
                    "response": response_text,
                    "state": session["state"],
                    "selected_game": session.get("selected_game"),
                }

            if not message:
                return {
                    "response": f"Pose-moi une question sur {session['selected_game']}.",
                    "state": session["state"],
                    "selected_game": session["selected_game"],
                }

            session["history"].append({"user": message})

            answer = self.handle_universe_question(session, message)

            session["history"].append({"bot": answer})

            session["history"] = session["history"][-40:]

            return {
                "response": answer,
                "state": session["state"],
                "selected_game": session["selected_game"],
            }

        session["state"] = ConversationState.ASKING_UNIVERSE
        session["selected_game"] = None

        return {
            "response": "Une erreur s'est produite. Recommençons. Sur quel univers Endless veux-tu que je t'aide ?",
            "state": session["state"],
            "selected_game": None,
        }

    def reset_session(self, session_id: str) -> Dict[str, str]:
        if session_id in self.chat_sessions:
            self.chat_sessions.pop(session_id)

        return {
            "message": "Session réinitialisée avec succès",
            "response": "Bonjour ! Sur quel univers Endless d'Amplitude Studios veux-tu que je t'aide ?",
        }

    def get_session_info(self, session_id: str) -> Dict[str, Any]:
        session = self.chat_sessions.get(session_id)

        if not session:
            return {"exists": False, "message": "Session non trouvée"}

        return {
            "exists": True,
            "state": session["state"],
            "selected_game": session.get("selected_game"),
            "history_length": len(session["history"]),
            "last_messages": session["history"][-4:] if session["history"] else [],
        }

    def get_health_status(self) -> Dict[str, Any]:
        return {
            "status": "OK",
            "active_sessions": len(self.chat_sessions),
            "supported_universes": self.ENDLESS_UNIVERSES,
        }
