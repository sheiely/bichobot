import os
import json
import time
import requests 
import redis
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
RASA_WEBHOOK = os.getenv("RASA_WEBHOOK", "http://localhost:5005/webhooks/rest/webhook")
API_TOKEN = os.getenv("API_TOKEN")
redis_conn = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def generate_response_ollama(query, context, max_length=3000):
    input_text = f"Pergunta: {query}\nContexto: {context}"
    payload = {
        "model": "llama3",
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
        "max_tokens": 3000,
        "stream": False
        }

    try:
        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post(OLLAMA_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Erro na LLM: {e}")
        return "Ocorreu um erro ao gerar a resposta."

def send_message_to_user(chat_id, message):
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")

def worker_loop():
    while True:
        task_json = redis_conn.lpop("llm_tasks")
        
        if task_json:
            task = json.loads(task_json)
            sender_id = task["sender_id"]
            query = task["query"]
            context = task["context"]
            response = generate_response_ollama(query, context)
            send_message_to_user(sender_id, response)
        else:
            time.sleep(1)

if __name__ == "__main__":
    worker_loop()
