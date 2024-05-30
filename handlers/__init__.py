from aiogram import Dispatcher

from handlers import start


async def setup_handlers(dp: Dispatcher):
    dp.include_routers(start.router)
