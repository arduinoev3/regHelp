from server.llms.giga_chat import giga_chat_llm
from server.llms.llms_type import LLMsType


def get_llm_by_type(type: LLMsType):
    match (type):
        case LLMsType.GigaChat:
            return giga_chat_llm()
