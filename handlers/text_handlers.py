from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(F.text == '🌤️ Weather')
async def cmd_text_weather(message: Message):
    await message.answer('Today is sunny +22°C ☀️')


@router.message(F.text == '📰 News')
async def cmd_text_news(message: Message):
    await message.answer('Today is Action! 🚀')


@router.message(F.text == '⚙️ Settings')
async def cmd_text_settings(message: Message):
    await message.answer('⚙️ Settings')


@router.message(F.text == '❌ Close Menu')
async def cmd_text_close_menu(message: Message):
    await message.answer('❌ Menu closed', reply_markup=ReplyKeyboardRemove())


@router.message(F.text)
async def cmd_text_handler(message: Message):
    """
    Handles all text messages and provides specific responses.
    """
    text = message.text.lower()

    if text == "hello":
        await message.answer("Hello, nice to see you!")
    elif text.startswith("how are you"):
        await message.answer("Fine, thanks!😊")
    else:
        # If no other condition is met, echo the message
        await message.answer(f"You said: {message.text}")

