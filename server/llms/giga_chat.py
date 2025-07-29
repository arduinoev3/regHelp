
import os
from dotenv import load_dotenv
from langchain_gigachat import GigaChat


def giga_chat_llm():
    load_dotenv()
    RUSSIAN_CERTIFICATE_PATH = os.getenv("RUSSIAN_CERTIFICATE_PATH")
    GIGA_CHAT_TOKEN = os.getenv("GIGA_CHAT_TOKEN")
    return GigaChat(
        credentials=GIGA_CHAT_TOKEN,
        ca_bundle_file=RUSSIAN_CERTIFICATE_PATH
    )