import logging
import aiohttp
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("API_TOKEN")
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    payload = {
        "sender": str(message.from_user.id),
        "message": message.text
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(RASA_URL, json=payload) as resp:
                rasa_response = await resp.json()

        if rasa_response:
            for r in rasa_response:
                if "text" in r:
                    await message.answer(r["text"])
        else:
            await message.answer("Desculpe, não entendi.")

    except Exception as e:
        logging.exception("Erro ao falar com o Rasa:")
        await message.answer("Ocorreu um erro ao se comunicar com o assistente.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
