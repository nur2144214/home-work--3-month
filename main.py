from config import bot, dp
from aiogram import executor, types
import logging
from handlers import commands, quiz


commands.register_commands(dp)
quiz.register_handler_quiz(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, allowed_updates=['callback'])