from typing import List
from langchain_core.embeddings import Embeddings

class BGEM3Embeddings(Embeddings):
    def __init__(self):
        from FlagEmbedding import BGEM3FlagModel
        self.model = BGEM3FlagModel("BAAI/bge-m3", use_fp16=False)

    def embed_documents(self, texts: list[str]) -> List[List[float]]:
        return self.model.encode(texts, return_dense=True)["dense_vecs"].tolist()

    def embed_query(self, text: str) -> List[float] :
        return self.model.encode(text, return_dense=True)["dense_vecs"].tolist()