from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from models.user import User

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    if not await User.exists(id=message.from_user.id):
        await User.create_user(message.from_user)
    await message.answer(f"Hello, {message.from_user.first_name}")
