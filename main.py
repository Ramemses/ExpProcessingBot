import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

from config import settings
from handlers import user_router


logger = logging.getLogger(__name__)


# def get_greeting():
#     return "Привет, чепуха"

# def my_wrapper():
#     return "Я не ебу че ты пишешь"

# @dispatcher.message(Command(commands="start"))
# async def process_start_command(message: Message):
#     response = get_greeting()
#     await message.answer(response)

# @dispatcher.message()
# async def process_start_command(message: Message):
#     response = my_wrapper()
#     await message.answer(response)


async def main():
    logging.basicConfig(level=settings.log.level,
                         format=settings.log.format
                         )

    logger.info('Starting bot')



    bot = Bot(token=settings.bot.token)
    dispatcher = Dispatcher()




    logger.info('Connect routes')
    dispatcher.include_router(user_router)  



    logger.info('Connect middlewares')


    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)



asyncio.run(main())