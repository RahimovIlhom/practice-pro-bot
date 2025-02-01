from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from data.config import WEB_APP_URL
from loader import dp


@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.answer(
        "👇 Quyidagi tugma orqali Amaliyot platformasiga kiring",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🚀 Amaliyot Platformasiga Kirish", web_app=WebAppInfo(url=WEB_APP_URL))]
            ],
            resize_keyboard=True
        )
    )
