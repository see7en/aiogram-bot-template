from loguru import logger
from tortoise import Tortoise

from utils.database import init_db


async def on_startup() -> None:
    logger.debug("Bot is starting...")
    await init_db()


async def on_shutdown():
    logger.debug("Bot is shutting down...")
    await Tortoise.close_connections()
