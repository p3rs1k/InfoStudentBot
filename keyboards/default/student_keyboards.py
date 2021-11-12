from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton

student_keyword = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Зареєструватись"),
         ],
        [
            KeyboardButton(text="Продовжити без реєстрації"),
        ],
    ],
    resize_keyboard=True,
)

all_student_keyword1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оплатити проживання"),
         ],
        [
            KeyboardButton(text="Оплатити інтернет зв\'язок"),
        ],
        [
            KeyboardButton(text="Друк документів"),
        ],
        [
            KeyboardButton(text="На головну"),
            KeyboardButton(text="Далі"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

all_student_keyword2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Онлайн прання"),
        ],
        [
            KeyboardButton(text="Процедура поселення"),
        ],
        [
            KeyboardButton(text="Процедура виселення на літо"),
        ],
        [
            KeyboardButton(text="На головну"),
            KeyboardButton(text="Назад"),
        ],

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)