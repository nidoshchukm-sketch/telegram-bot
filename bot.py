import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8575469494:AAE_ImdyVaKc4XdZN6Tj6XD0ij29kB2rnoY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Бот работает")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
