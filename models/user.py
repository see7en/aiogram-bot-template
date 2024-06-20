from loguru import logger
from tortoise import fields, models
from aiogram.types import User as TelegramUser


class User(models.Model):
    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=255, null=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255, null=True)

    language_code = fields.CharField(max_length=10, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"

    @staticmethod
    async def create_user(telegram_user: TelegramUser) -> 'User':
        user = await User.create(
            id=telegram_user.id,
            first_name=telegram_user.first_name,
            last_name=telegram_user.last_name,
            username=telegram_user.username,
            language_code=telegram_user.language_code
        )
        logger.success(f"{user} created")
        return user

    def __str__(self):
        return f"User(id={self.id}, first_name={self.first_name})"
