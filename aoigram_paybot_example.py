import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import LabeledPrice
from aiogram.filters import Command
import asyncio

from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("buy"))
async def buy_service(message: types.Message):
    prices = [LabeledPrice(label="XTR", amount=10)]
    await message.answer_invoice(
        title="Покупка услуги",
        description="Оплата услуги в боте",
        prices=prices,
        provider_token="",
        currency="XTR",
        payload="buy_service"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())