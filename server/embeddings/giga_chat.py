import os
from dotenv import load_dotenv
from langchain_gigachat import GigaChatEmbeddings


def giga_chat_embeddings():
    load_dotenv()
    RUSSIAN_CERTIFICATE_PATH = os.getenv("RUSSIAN_CERTIFICATE_PATH")
    GIGA_CHAT_TOKEN = os.getenv("GIGA_CHAT_TOKEN")
    return GigaChatEmbeddings(
        credentials=GIGA_CHAT_TOKEN,
        ca_bundle_file=RUSSIAN_CERTIFICATE_PATH
    )