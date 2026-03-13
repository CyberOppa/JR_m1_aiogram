from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def menu_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🌤️ Weather'),
                KeyboardButton(text='📰 News'),
            ],
            [
                KeyboardButton(text='⚙️ Settings')
            ],
            [
                KeyboardButton(text='❌ Close Menu')
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder='choose an option of keyboard',
    )

    return keyboard


def special_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Sent my phone number', request_contact=True)
            ],
            [
                KeyboardButton(text='Sent my geolocation', request_location=True)
            ],
            [
                KeyboardButton(text='❌ Close Menu',reply_markup=ReplyKeyboardRemove())
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder='choose an option of keyboard',
    )

    return keyboard
