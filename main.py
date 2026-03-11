from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import logging
import asyncio

bot: Bot = Bot(token=BOT_TOKEN)  # Create a bot instance
dp: Dispatcher = Dispatcher()    # Handeln updates, events

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
