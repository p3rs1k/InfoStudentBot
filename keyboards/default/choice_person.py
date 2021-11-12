from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton



person = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Адміністратор"),
            KeyboardButton(text="Студент"),
         ],
    ],
    resize_keyboard=True,
)


