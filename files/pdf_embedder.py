from langchain_text_splitters import CharacterTextSplitter
from langchain_weaviate import WeaviateVectorStore
import weaviate
from langchain_community.document_loaders import PyPDFLoader

from embeddings.get_embeddings_by_model import CURRENT_EMBEDDINGS
from files.embedder import Embedder

class PdfEmbedder(Embedder):
    def __init__(self):
        pass

    async def embed_file(self, file_path):
        docs = PyPDFLoader(file_path).load()
        text_splitter = CharacterTextSplitter(chunk_size=384, chunk_overlap=200)
        docs = text_splitter.split_documents(docs)
        weaviate_client = weaviate.connect_to_local()
        WeaviateVectorStore.from_documents(docs, CURRENT_EMBEDDINGS, client=weaviate_client, index_name='db', text_key='text')
        weaviate_client.close()