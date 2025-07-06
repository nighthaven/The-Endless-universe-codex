from enum import Enum

class ConversationState(str, Enum):
    ASKING_UNIVERSE = "asking_universe"
    UNIVERSE_READY = "universe_ready"
