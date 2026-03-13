from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def demo_inline():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Push me', callback_data='btn:hello'),
                InlineKeyboardButton(text='Google', url='https://google.com')
            ]
        ]
    )

    return keyboard