import os
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from qdrant_client.models import Distance, VectorParams, PointStruct
from get_embedding_Qdrant import get_embedding
from langchain.document_loaders import PyPDFLoader, TextLoader
import fitz  # PyMuPDF
import argparse

# 🔹 Configuração do Qdrant (Rodando localmente)
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "documentos_academicos"
client = QdrantClient(url=QDRANT_URL)
embedder = get_embedding()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    if(not client.collection_exists(COLLECTION_NAME)):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=embedder.get_sentence_embedding_dimension(), distance=Distance.COSINE),
        )
    docs = load_documents("./data")
    payloads = split_documents(docs)

    points = []
    for i, payload in enumerate(payloads):
        if(not check_if_exists(payload)):
            embedding = embedder.encode(payload["page_content"]).tolist()
            points.append(PointStruct(id=i, vector=embedding, payload=payload))
        else:
            print("documento desse payload ja esta no banco de dados")


    client.upsert(collection_name=COLLECTION_NAME, points=points)

    print(f"✅ Banco vetorial criado com {len(points)} points!")

    # 🔹 Exemplo de busca
    query = "Que dia começa as ferias?"
    resultados = search_qdrant(query)
    print("\n🔍 Resultados da Busca:\n")
    for r in resultados:
        print("_------------------------------")  # Mostrando só os primeiros 200 caracteres
        print(r)
    


# 🔹 Função de busca semântica
def search_qdrant(query, top_k=3):
    query_embedding = embedder.encode(query).tolist()
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_embedding,
        limit=top_k,
    )
    return [hit.payload["page_content"] for hit in results]




def clear_database():
    client.delete_collection(collection_name=COLLECTION_NAME)
    client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=embedder.get_sentence_embedding_dimension(), distance=Distance.COSINE),
        )


def load_documents(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif file.endswith(".txt"):
            loader = TextLoader(file_path)
        else:
            continue
        
        docs = loader.load()
        documents.extend(docs)
    return documents

def split_documents(docs):
    payloads = []

    for document in docs:
        source = document.metadata["source"]
        if source.endswith(".pdf"):
            doc = fitz.open(source)
            page = doc.load_page(document.metadata['page'])
            blocks = page.get_text("blocks")
            paragraphs = []
            current_paragraph = ""
            for block in blocks:
                text = block[4]
                if text.strip() == '':
                    current_paragraph += text.strip() + " "
                else:
                    paragraphs.append(current_paragraph + text.strip())
                    current_paragraph = ""
            if current_paragraph.strip() != "":
                paragraphs.append(current_paragraph.strip())

            page_label = 1
            for paragraph in paragraphs:
                payload = {
                    "page_content": paragraph,
                    "metadata": {
                        "source": source,
                        "page": document.metadata["page"] + 1,
                        "page_label": page_label
                    }
                }
                page_label += 1
                payloads.append(payload)

        elif source.endswith(".txt"):
            print("opa um txt")
            payload = {
                "page_content": document.page_content,
                "metadata": {
                    "source": source,
                    "page": 1,
                    "page_label": 1
                }
            }
            print(payload)
            payloads.append(payload)

    return payloads


def check_if_exists(payload):
    filter = Filter(
        must=[ 
            FieldCondition(
               key='metadata.source',
               match= MatchValue(value=payload['metadata']['source'])
            )
      ])
    result = client.scroll(collection_name=COLLECTION_NAME, scroll_filter=filter, limit=1)
    return len(result[0])>0


if __name__ == "__main__":
    main()