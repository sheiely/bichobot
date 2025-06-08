from sentence_transformers import SentenceTransformer

def get_embedding():
    EMBEDDING_MODEL = "hkunlp/instructor-xl"
    return SentenceTransformer(EMBEDDING_MODEL)
