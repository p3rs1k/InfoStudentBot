from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

registration = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Авторизуватись"),
         ],
    ],
    resize_keyboard=True,
)


admin_panel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Знайти студента"),
        ],
        [
            KeyboardButton(text="Написати студентам з кімнати"),
        ],
        [
            KeyboardButton(text="Розіслати усім"),
        ],
        [
            KeyboardButton(text="На головну"),
        ],
    ],
    resize_keyboard=True,
)


to_home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="На головну"),
        ],

    ],
    resize_keyboard=True,
)
