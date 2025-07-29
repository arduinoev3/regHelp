import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_weaviate import WeaviateVectorStore
import weaviate
from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader
from server.embeddings.get_embeddings_by_type import CURRENT_EMBEDDINGS

class FileEmbedder:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=384, chunk_overlap=200)

    async def embed_file(self, file_path: str):
        docs = self.load_document(file_path=file_path)
        docs = self.text_splitter.split_documents(docs)
        dense_documents = [
            Document(
                page_content=chunk.page_content,
                metadata={
                    "source": file_path,
                    "chunk_number": i
                }
            )
            for i, chunk in enumerate(docs)
        ]
        weaviate_client = weaviate.connect_to_local()
        WeaviateVectorStore.from_documents(dense_documents, CURRENT_EMBEDDINGS, client=weaviate_client, index_name='db', text_key='text')
        weaviate_client.close()

    def load_document(self, file_path: str):
        _, extension = os.path.splitext(file_path)
        print(f'Загрузка документа {file_path}')
        match extension:
            case ".pdf":
                return PyPDFLoader(file_path).load()
            case ".docx":
                return UnstructuredWordDocumentLoader(file_path).load()
        raise Exception(f"Got wrong file extension while embedding file {file_path}")