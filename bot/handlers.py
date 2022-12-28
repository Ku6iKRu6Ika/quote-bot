from bot.dispatcher import dp
from bot.utils import create_quote_photo
from aiogram import types


@dp.message_handler(commands=['random_quote'])
async def random_quote(message: types.Message):
    await message.reply_photo(photo=create_quote_photo())
