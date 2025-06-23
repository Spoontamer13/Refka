from aiogram import Bot, Dispatcher, types 
from aiogram.types import FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import os

BOT_TOKEN = os.getenv("7587562761:AAEaM1746z0ZknDG3Gn2D6MgsbrL_7tn0o4")

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

@dp.message(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет! Чтобы получить PDF-гайд, отправь команду /получить")

@dp.message(commands=["получить"])
async def send_pdf(message: types.Message):
    file = FSInputFile("guide.pdf")
    await message.answer_document(file, caption="Вот твой гайд 📄")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())