from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import CHAT_ID
from loader import dp
from states import Client_state


@dp.message_handler(Command("support"))
async def bot_start(message: types.Message):
    await message.answer("Опишите, пожалуйста, проблему и ожидайте ответа:")
    await Client_state.S1.set()


@dp.message_handler(state=Client_state.S1, content_types=types.ContentTypes.ANY)
async def send_to_group(message: types.Message, state: FSMContext):
    await message.forward(chat_id=CHAT_ID)
    await state.finish()





