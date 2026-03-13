from aiogram import Router
from handlers.commands_handler import router as command_router
from handlers.text_handlers import router as text_router
from handlers.voice_handler import router as voice_router
from handlers.callbacks_handler import router as callback_router


router = Router()

router.include_routers(command_router, text_router, voice_router, callback_router)