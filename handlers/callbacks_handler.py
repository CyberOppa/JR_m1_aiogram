from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

router = Router()


@router.callback_query(F.data == 'btn:hello')
async def cmd_btn_hello(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('You have pushed the button')