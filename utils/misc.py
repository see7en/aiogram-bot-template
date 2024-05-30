import logging


async def on_startup() -> None:
    logging.debug("Bot is starting...")


async def on_shutdown():
    logging.debug("Bot is shutting down...")
