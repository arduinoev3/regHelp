from server.llms.get_llm_by_type import get_llm_by_type
from server.llms.llms_type import LLMsType


CURRENT_LLM = get_llm_by_type(LLMsType.GigaChat)