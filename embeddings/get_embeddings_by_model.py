import os
from dotenv import load_dotenv
from embeddings.all_mini_lm import all_mini_lm_embeddings
from embeddings.bge_m3 import BGEM3Embeddings
from embeddings.embeddings_type import EmbeddingsType
from embeddings.giga_chat import giga_chat_embeddings

load_dotenv()
GIGA_CHAT_TOKEN = os.getenv("GIGACHAT_API_KEY")

def get_embeddings_by_model(model: EmbeddingsType):
    match (model):
        case EmbeddingsType.AllMiniLM:
            return all_mini_lm_embeddings()
        case EmbeddingsType.BGEM3:
            return BGEM3Embeddings()
        case EmbeddingsType.GigaChat:
            return giga_chat_embeddings(GIGA_CHAT_TOKEN)


CURRENT_EMBEDDINGS = get_embeddings_by_model(EmbeddingsType.BGEM3)