from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

def all_mini_lm_embeddings():
    return SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")