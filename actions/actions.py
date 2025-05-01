from rasa_sdk import Action
from rasa_sdk.events import UserUtteranceReverted
import requests
from qdrant_client import QdrantClient
from actions.get_embedding_Qdrant import get_embedding
from dotenv import load_dotenv
import os
load_dotenv()
# 🔹 Configurações
QDRANT_URL = os.getenv("QDRANT_URL")
COLLECTION_NAME = "documentos_academicos"
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

client = QdrantClient(url=QDRANT_URL)
embedder = get_embedding()

class ActionFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get("text")  # Última mensagem do usuário
        
        # 🔹 Busca os documentos mais relevantes no Qdrant
        context = self.search_qdrant(user_message)

        # 🔹 Gera a resposta usando o contexto obtido
        self.generate_response_with_ollama(dispatcher, user_message, context)

        return [UserUtteranceReverted()]  # Evita que a interação fique no histórico

    def search_qdrant(self, query, top_k=5):
        """Busca no Qdrant os documentos mais relevantes para a consulta."""
        query_embedding = embedder.encode(query).tolist()
        results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=top_k,
        )
        return " ".join([hit.payload["page_content"] for hit in results])

    def generate_response_with_ollama(self, dispatcher, query, context, max_length=3000):
        input_text = f"Pergunta: {query}\nContexto: {context}"
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {
                "role": "system",
                "content": "Você é um assistente especializado que responde com base no contexto fornecido. Se o contexto não contiver a resposta, apenas diga 'Não sei' e não invente informações. Seja direto e objetivo."
                },
                {
                "role": "user",
                "content": input_text
                }
            ],
            "temperature": 0.1,
            "top_p": 0.95,
            "presence_penalty": 0.0,
            "frequency_penalty": 0.0,
            "max_tokens": max_length,
            "stream": False
        }
        headers = {"Content-Type": "application/json"}
        print(OLLAMA_URL)
        response = requests.post(OLLAMA_URL, json=payload, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            message = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
            dispatcher.utter_message(text=message)
        else:
            print(response)
            dispatcher.utter_message(text="Ocorreu um erro ao buscar a resposta.")
