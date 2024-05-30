from loguru import logger


async def on_startup() -> None:
    logger.debug("Bot is starting...")


async def on_shutdown():
    logger.debug("Bot is shutting down...")
