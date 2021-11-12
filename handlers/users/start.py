from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.choice_person import person

from loader import dp


@dp.message_handler(commands="start")
async def bot_start(message: Message):
    await message.answer(
        f"Привіт, {message.from_user.full_name}!\n"
        f"Виберіть сценарій: ",
        reply_markup=person
    )




