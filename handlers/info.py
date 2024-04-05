from aiogram import Router, types
from aiogram.filters import Command
info_router = Router()


@info_router.message(Command('myinfo'))
async def info(message: types.Message):
    await message.reply(f'Hello, {message.from_user.first_name} \n'
                        f'Your name is {message.from_user.first_name} \n'
                        f'Your id is {message.from_user.id}')