from typing import Any

from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager

from medsyncapp.tgbot.config import Config
from medsyncapp.tgbot.keyboards.inline import main_menu

start_router = Router()


@start_router.message(CommandStart())
async def send_webapp(message: types.Message, config: Config):
    await message.answer(
        "MedBrand ilovasiga xush kelibsiz!\n\n"
        "Web-ilovamiz orqali shifokor qabuliga yozilishingiz yoki klinikalarimizdan birida tahlil topshirishingiz mumkin.",
        reply_markup=main_menu(domain=config.tg_bot.web_app_domain),
    )


async def start_from_dialog_menu(
    callback_query:types.CallbackQuery, widget: Any, dialog_manager: DialogManager
):
    config: Config = dialog_manager.middleware_data.get("config")
    await callback_query.message.answer(
        "MedBrand ilovasiga xush kelibsiz!\n\n"
        "Web-ilovamiz orqali shifokor qabuliga yozilishingiz yoki klinikalarimizdan birida tahlil topshirishingiz mumkin.",
        reply_markup=main_menu(domain=config.tg_bot.web_app_domain),
    )
