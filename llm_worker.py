import os
import json
import time
import requests  # Troquei para requests
import redis
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
RASA_WEBHOOK = os.getenv("RASA_WEBHOOK", "http://localhost:5005/webhooks/rest/webhook")  # porta padrão

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
            "content": "Pergunta: manda o link pro calendario \n Contexto: link pro calendario: facebppl.com"
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
        response.raise_for_status()  # Levanta exceção para erros HTTP
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Erro na LLM: {e}")
        return "Ocorreu um erro ao gerar a resposta."

TELEGRAM_BOT_TOKEN = '8040579065:AAEo5q0EXvWw-ZgbBiXMuRhlBTXw9y4HkP0'

def send_message_to_user(chat_id, message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
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
    print("Worker iniciado. Aguardando tarefas...")
    while True:
        task_json = redis_conn.lpop("llm_tasks")
        
        if task_json:
            task = json.loads(task_json)
            sender_id = task["sender_id"]
            query = task["query"]
            context = task["context"]

            print(f"⏳ Processando pergunta de {sender_id}: {query}")
            response = generate_response_ollama(query, context)
            send_message_to_user(sender_id, response)
            print(f"✅ Resposta enviada para {sender_id}")
        else:
            time.sleep(1)

if __name__ == "__main__":
    worker_loop()
