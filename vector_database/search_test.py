from qdrant_client import QdrantClient
from get_embedding_Qdrant import get_embedding

# 🔹 Configuração do Qdrant (Rodando localmente)
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "documentos_academicos"
client = QdrantClient(url=QDRANT_URL)
embedder = get_embedding()

def main():

    # 🔹 Exemplo de busca
    query = "Que dia começa as ferias?"
    resultados = search_qdrant(query)
    print("\n🔍 Resultados da Busca:\n")
    for r in resultados:
        print("_------------------------------")  # Mostrando só os primeiros 200 caracteres
        print(r)


def search_qdrant(query, top_k=3):
    query_embedding = embedder.encode(query).tolist()
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k,
    )
    return [hit.payload["page_content"] for hit in results]


if __name__ == "__main__":
    main()