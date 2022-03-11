from aiogram import types

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.ANY)
async def support_answer(message: types.Message):
    try:
        user_id = message.reply_to_message.forward_from.id
        await message.copy_to(user_id)
    except AttributeError:
        pass
