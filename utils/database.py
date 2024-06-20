from tortoise import Tortoise
from loguru import logger

from utils.config import Settings


async def init_db() -> None:
    settings = Settings()
    logger.info("Initializing the database...")
    await Tortoise.init(
        db_url=settings.db_url,
        modules={'models': ['models.user']}
    )
    await Tortoise.generate_schemas()
