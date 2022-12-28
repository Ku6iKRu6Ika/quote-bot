from aiogram import executor
from bot.dispatcher import dp
import bot.handlers
import logging

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    executor.start_polling(dp)
