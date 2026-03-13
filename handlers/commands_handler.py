from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, Chat
from aiogram.fsm.context import FSMContext
from states.states import RegistrationProfile
from utils.file_handler import save_user_data, get_user_from_file  # Import get_user_from_file
from keyboards.reply import menu_keyboard, special_keyboard
from keyboards.inline import demo_inline

router = Router()


@router.message(Command('menu'))
async def cmd_menu(message: Message):
    keyboard = menu_keyboard()
    await message.answer('Menu', reply_markup=keyboard)


@router.message(Command('special'))
async def cmd_special(message: Message):
    keyboard = special_keyboard()
    await message.answer('Type to send your data', reply_markup=keyboard)


# start command handler and registration
@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    
    # 1. check if user is already registered
    existing_user = get_user_from_file(message.from_user.id)
    
    if existing_user:
        # user found, already registered
        # existing_user example: {'user_id': 123, 'username': '...', 'data': {'name': 'Alex', ...}}
        user_name = existing_user['data'].get('name', 'User')
        await message.answer(f"Willkommen zurück, {user_name.capitalize()}! 😍\nDu bist bereits registriert.")
        #
    else:
        # if user not found -> Registration start
        await message.answer("Hello! I'm your aiogram bot! 😍 \n\nLet us set your Profile\n\nStep 1:\nWhat is your Name?")
        await state.set_state(RegistrationProfile.waiting_name)

# register cancel
@router.message(Command('cancel'))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Your input was canceled.")


@router.message(Command('demo'))
async def cmd_demo(message: Message):
    keyboard = demo_inline()
    await message.answer('inline keyboard', reply_markup=keyboard)


# register name
@router.message(RegistrationProfile.waiting_name)
async def cmd_waiting_name(message: Message, state: FSMContext):
    await message.answer(f"Nice to meet you, {message.text.capitalize()}!😊 \n\nStep 2:\nHow old are you?")
    await state.update_data(name=message.text)
    await state.set_state(RegistrationProfile.waiting_age)

# register age
@router.message(RegistrationProfile.waiting_age)
async def cmd_waiting_age(message: Message, state: FSMContext):
    await message.answer(f"Your Age {message.text.capitalize()} was saved.\n\nStep 3:\nWhere are you from?")
    await state.update_data(age=message.text)

    await state.set_state(RegistrationProfile.waiting_city)

# register city
@router.message(RegistrationProfile.waiting_city)
async def cmd_waiting_city(message: Message, state: FSMContext):
    await message.answer(f"Your City {message.text.capitalize()} was saved.")
    await state.update_data(city=message.text)

    data = await state.get_data()
    # Simple list comprehension to create lines
    data_lines = [f"{key.capitalize()}: {value.capitalize()}" for key, value in data.items()]
    formatted_data = "\n".join(data_lines)
    await message.answer(f"Registry was successfully, this is your data: \n\n{formatted_data}")

    # Verwende jetzt die neue Hauptfunktion, die alles erledigt
    save_user_data(message.from_user.id, message.from_user.username, data)

    await state.clear()


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
