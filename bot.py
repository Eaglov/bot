# bot.py
import os
import random
import string
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("API_TOKEN", "8491049225:AAHGsmLEgAX7mMLfIXGzaz-U-CGgzmk6Vfg")
FRONT_URL = os.getenv("FRONT_URL", "https://game-front-two.vercel.app/webapp.html")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def gen_room_id():
    # короткий удобный код: 6 символов [A-Z0-9]
    alphabet = string.ascii_uppercase + string.digits
    return "".join(random.choice(alphabet) for _ in range(6))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    room_id = gen_room_id()
    url = f"{FRONT_URL}?roomId={room_id}"

    kb = InlineKeyboardMarkup().add(
        InlineKeyboardButton("🎉 Открыть игру", web_app=WebAppInfo(url=url))
    )

    await message.answer(
        "Привет! Это party-game. Нажми кнопку, чтобы открыть мини-приложение Telegram.\n\n"
        f"Код твоей комнаты: <b>{room_id}</b>\n"
        "Поделись им с друзьями, чтобы они присоединились.",
        parse_mode="HTML",
        reply_markup=kb
    )

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
