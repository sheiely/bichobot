from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted
from qdrant_client import QdrantClient
from actions.get_embedding_Qdrant import get_embedding
from dotenv import load_dotenv
import os
import redis
import json

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
COLLECTION_NAME = "documentos_academicos"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

redis_conn = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
client = QdrantClient(url=QDRANT_URL)
embedder = get_embedding()

class ActionFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")
        sender_id = tracker.sender_id

        context = self.search_qdrant(user_message)

        task = {
            "sender_id": sender_id,
            "query": user_message,
            "context": context
        }

        redis_conn.rpush("llm_tasks", json.dumps(task))

        dispatcher.utter_message("Estou analisando sua pergunta. Enviarei a resposta em breve.")
        return [UserUtteranceReverted()]

    def search_qdrant(self, query, top_k=5):
        query_embedding = embedder.encode(query).tolist()
        results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=top_k,
        )
        return " ".join([hit.payload["page_content"] for hit in results])
