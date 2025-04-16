from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("6324958627:AAGaz8WxBLzOZA16I-JeR9VqPxRXHPimyvU")  # или просто вставь свой токен как строку

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Запустить игру", web_app=WebAppInfo(url="https://myvirustg.onrender.com"))]
    ])
    await message.answer("Добро пожаловать! Нажми кнопку, чтобы начать:", reply_markup=keyboard)

if __name__ == "__main__":
    from aiogram import executor
    from dotenv import load_dotenv
    load_dotenv()
    executor.start_polling(dp)
