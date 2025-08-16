from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu(domain: str):
    kb = InlineKeyboardBuilder()
    kb.button(text="Asosiy sahifa", web_app=WebAppInfo(url=domain))
    kb.button(
        text="📅 Uchrashuv bron qilish",
        web_app=WebAppInfo(url=f"{domain}/see_a_doctor"),
    )
    kb.button(
        text="📝 Tahlil topshirish",
        web_app=WebAppInfo(url=f"{domain}/get_tested"),
    )
    kb.button(text="📋 Mening bronlarim", callback_data="my_bookings")
    kb.button(text="📋 Tahlil natijalari", callback_data="my_results")
    kb.adjust(1, 2, 2)
    return kb.as_markup()


