import os
from dotenv import load_dotenv
from embeddings.all_mini_lm import all_mini_lm_embeddings
from embeddings.bge_m3 import BGEM3Embeddings
from embeddings.embeddings_type import EmbeddingsType
from embeddings.giga_chat import giga_chat_embeddings

def get_embeddings_by_type(type: EmbeddingsType):
    match (type):
        case EmbeddingsType.AllMiniLM:
            return all_mini_lm_embeddings()
        case EmbeddingsType.BGEM3:
            return BGEM3Embeddings()
        case EmbeddingsType.GigaChat:
            return giga_chat_embeddings()
