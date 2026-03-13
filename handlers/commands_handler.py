from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, Chat

router = Router()


# start command
@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer("Hello! I'm your aiogram bot! 😍")


# help command
@router.message(Command('help'))
async def cmd_help(message: Message):
    help_text = '''
    Available Commands:
    /start - Start the bot
    /help - Show this help message
    /info - Get information about the bot
    /whoami - Configure bot settings
    /stats - Get bot statistics
    '''
    await message.answer(help_text)


# info command
@router.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer("I'm a simple aiogram Bot with a few ChatGPT functions.")


# whoami command
@router.message(Command('whoami'))
async def cmd_whoami(message: Message):
    user = message.from_user

    info = (
        f"User ID: {user.id}\n"
        f"Username: {user.username}\n"
        f"First Name: {user.first_name or 'Not available'}\n"
        f"Last Name: {user.last_name or 'Not available'}\n"
        f"Is Bot: {user.is_bot}\n"
        f"Language Code: {user.language_code or 'Not available'}\n"
        f"Is Premium: {user.is_premium or False}\n\n"
        f"Chat ID: {message.chat.id}\n"
        f"Chat Type: {message.chat.type}\n")
    await message.answer(str(info))


# stats command
@router.message(Command('stats'))
async def cmd_stats(message: Message):
    chat: Chat = message.chat


