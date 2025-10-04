import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode

from config import settings
from handlers import user_router, direct_record_router


logger = logging.getLogger(__name__)



async def main():
    logging.basicConfig(level=settings.log.level,
                         format=settings.log.format
                         )

    logger.info('Starting bot')



    bot = Bot(token=settings.bot.token)
    dispatcher = Dispatcher()




    logger.info('Connect routes')
    dispatcher.include_router(user_router)  
    dispatcher.include_router(direct_record_router)  



    logger.info('Connect middlewares')

    logger.info('Delete webhooks')
    await bot.delete_webhook(drop_pending_updates=True)


    logger.info('Start polling')
    await dispatcher.start_polling(bot)



asyncio.run(main())