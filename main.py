from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, Chat
from aiogram import F
from config import BOT_TOKEN
import asyncio
import logging
from handlers.commands_handler import router as command_router
from handlers.text_handlers import router as text_router


async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s')
    bot = Bot(token=BOT_TOKEN)  # Create a bot instance
    dp = Dispatcher()  # Handeln updates, events
    dp.include_routers(command_router, text_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
