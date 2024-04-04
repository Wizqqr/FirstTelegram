from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import os
from random import choice
from config import bot
random_pic_router = Router()
@random_pic_router.message(Command('photo'))
async def photo(message: types.Message):
    chat_id = message.from_user.id
    path = 'images/1!!.jpg'
    file = FSInputFile(path)
    await bot.send_photo(chat_id=chat_id, photo=file, caption='GOAT')


@random_pic_router.message(Command('random'))
async def random(message: types.Message):
    photos = os.listdir('images/')
    path = f'images/{choice(photos)}'
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='GOAT')


