from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

API_TOKEN = os.getenv("7587562761:AAEaM1746z0ZknDG3Gn2D6MgsbrL_7tn0o4")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer("Привет! Напиши /получить чтобы получить PDF-гайд")

@dp.message_handler(commands=["получить"])
async def send_pdf(message: types.Message):
    with open("guide.pdf", "rb") as doc:
        await message.answer_document(doc, caption="Вот твой гайд")

if __name__ == "__main__":
    executor.start_polling(dp)