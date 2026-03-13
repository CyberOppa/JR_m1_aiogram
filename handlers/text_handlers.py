from aiogram import Router, F
from aiogram.types import Message

router = Router()

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
