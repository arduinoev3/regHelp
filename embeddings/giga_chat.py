from langchain_gigachat import GigaChatEmbeddings


def giga_chat_embeddings(GIGA_CHAT_TOKEN):
    return GigaChatEmbeddings(
        credentials=GIGA_CHAT_TOKEN,
        verify_ssl_certs=False
    )