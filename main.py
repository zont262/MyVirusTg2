from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor
import os
import  uvicorn

BOT_TOKEN = os.getenv("6324958627:AAGaz8WxBLzOZA16I-JeR9VqPxRXHPimyvU")  # или просто вставь свой токен как строку

bot = Bot(token="6324958627:AAGaz8WxBLzOZA16I-JeR9VqPxRXHPimyvU")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Запустить игру", web_app=WebAppInfo(url="https://myvirustg.onrender.com"))]
    ])
    await message.answer("Добро пожаловать! Нажми кнопку, чтобы начать:", reply_markup=keyboard)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    from aiogram import executor
    from dotenv import load_dotenv
    load_dotenv()
    executor.start_polling(dp)
