from langchain_weaviate import WeaviateVectorStore
import weaviate
from langchain_gigachat.chat_models import GigaChat
from langchain_gigachat.embeddings.gigachat import GigaChatEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from dotenv import load_dotenv
import os

class GigaChatClient:
    rag_chain = None
    weaviate_client = None
    def __init__(self):
        load_dotenv()
        GIGA_CHAT_TOKEN = os.getenv("GIGACHAT_API_KEY")

        giga = GigaChat(
            credentials=GIGA_CHAT_TOKEN,
            verify_ssl_certs=False
        )

        embeddings = GigaChatEmbeddings(
            credentials=GIGA_CHAT_TOKEN,
            verify_ssl_certs=False
        )

        self.weaviate_client = weaviate.connect_to_local()
        vector_store = WeaviateVectorStore(
            client=self.weaviate_client, 
            index_name='db', 
            text_key='text',
            embedding=embeddings
        )

        retriever = vector_store.as_retriever()

        system_prompt_path = "input\\system_prompt.txt"
        system_prompt_text = open(system_prompt_path, "r", encoding='utf-8').read()
        system_prompt = system_prompt_text + "\n\n{context}"

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])

        question_answer_chain = create_stuff_documents_chain(giga, prompt)
        self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    async def get_answer(self, question: str):
        return self.rag_chain.invoke({"input": question})
    
    def close(self):
        self.weaviate_client.close()
    