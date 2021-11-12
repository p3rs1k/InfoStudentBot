import logging

from aiogram import Dispatcher
from aiogram.utils.exceptions import BotBlocked
# from handlers.errors.error_handler import errors_handler

from data.config import ADMINS



async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except BotBlocked:
            pass
        except Exception as err:
            logging.exception(err)


