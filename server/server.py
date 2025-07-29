from langchain_weaviate import WeaviateVectorStore
import weaviate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.retrieval import create_retrieval_chain
from langchain.retrievers.multi_query import MultiQueryRetriever
from server.embeddings.current_embeddings import CURRENT_EMBEDDINGS
from server.llms.current_llm import CURRENT_LLM

class Server:
    rag_chain = None
    weaviate_client = None
    def __init__(self):
        llm = CURRENT_LLM
        embeddings = CURRENT_EMBEDDINGS

        self.weaviate_client = weaviate.connect_to_local()
        vector_store = WeaviateVectorStore(
            client=self.weaviate_client, 
            index_name='db', 
            text_key='text',
            embedding=embeddings
        )

        retriever = MultiQueryRetriever.from_llm(
            retriever=vector_store.as_retriever(),
            llm=llm 
        )

        system_prompt_path = "input\\system_prompt.txt"
        with open(system_prompt_path, "r", encoding='utf-8') as file:
            system_prompt_text = file.read()
            file.close()
        system_prompt = system_prompt_text + "\n\n{context}"

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        self.rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    async def get_answer(self, question: str):
        return self.rag_chain.invoke({"input": question})['answer']
    
    def close(self):
        self.weaviate_client.close()

    def delete_index(self, index_name: str):
        self.weaviate_client.schema.delete_class(index_name)
    