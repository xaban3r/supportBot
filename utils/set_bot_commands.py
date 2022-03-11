from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Справка"),
            types.BotCommand("support", "Написать в поддержку")
        ]
    )
