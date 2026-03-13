from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import asyncio
import logging
from handlers import router


async def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s')
    bot = Bot(token=BOT_TOKEN)      # Create a bot instance
    dp = Dispatcher()               # Handeln updates, events
    dp.include_routers(router)      # Register routers from __init__.py
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
