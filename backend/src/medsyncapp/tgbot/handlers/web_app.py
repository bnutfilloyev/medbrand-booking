import json

from aiogram import Router, F, types
from aiogram.utils.markdown import hcode, hbold

from medsyncapp.infrastructure.database.repo.requests import RequestsRepo

web_app_router = Router()


@web_app_router.message(F.web_app_data)
async def bot_echo(message: types.Message, repo: RequestsRepo):
    data = json.loads(message.web_app_data.data)

    if data.get("action") == "booking_confirmed":
        booking_id = data.get("booking_id")
        booking_info = await repo.bookings.get_booking(int(booking_id))

        booking_time = booking_info.Booking.booking_time.strftime("%d %B %Y, %H:%M UTC")

        appointment_type_text = f"👨‍⚕️ <b>Shifokor:</b> {hbold(booking_info.Doctor.full_name)}\n" if booking_info.Doctor else f"🔬 <b>Diagnostika:</b> {hbold(booking_info.Diagnostic.type_name)}\n"

        await message.answer(
            text=f"🎉 <b>Tabriklaymiz! Sizning bronlaringiz tasdiqlandi!</b> ✅\n\n"
                 f"📋 <b>Bron ID:</b> {hcode(booking_id)}\n\n"
                 f"{appointment_type_text}"
                 f"📆 <b>Sana va vaqt:</b> {hbold(booking_time)}\n\n"
                 f"📍 <b>Manzil:</b> {hbold(booking_info.Location.name)}\n"
                 f"🏢 <i>{booking_info.Location.address}</i>\n\n"
                 f"🙏 <b>MedBrand xizmatini tanlaganingiz uchun rahmat!</b>\n"
                 f"📞 Savollaringiz bo'lsa yoki vaqtni o'zgartirish kerak bo'lsa, biz bilan bog'laning. 💬\n\n"
                 f"💚 <i>Sog'ligingiz bizning ustuvor vazifamiz!</i> 💚",
            parse_mode="HTML"
        )

    if data.get("action") == "booking_confirmed":
        booking_id = data.get("booking_id")
        booking_info = await repo.bookings.get_booking(int(booking_id))

        booking_time = booking_info.Booking.booking_time.strftime("%d %B %Y, %H:%M UTC")

        appointment_type_text = f"👨‍⚕️ <b>Shifokor:</b> {hbold(booking_info.Doctor.full_name)}\n" if booking_info.Doctor else f"🔬 <b>Diagnostika:</b> {hbold(booking_info.Diagnostic.type_name)}\n"

        await message.answer(
            text=f"🎉 <b>Tabriklaymiz! Sizning bronlaringiz tasdiqlandi!</b> ✅\n\n"
                 f"📋 <b>Bron ID:</b> {hcode(booking_id)}\n\n"
                 f"{appointment_type_text}"
                 f"📆 <b>Sana va vaqt:</b> {hbold(booking_time)}\n\n"
                 f"📍 <b>Manzil:</b> {hbold(booking_info.Location.name)}\n"
                 f"🏢 <i>{booking_info.Location.address}</i>\n\n"
                 f"🙏 <b>MedBrand xizmatini tanlaganingiz uchun rahmat!</b>\n"
                 f"📞 Savollaringiz bo'lsa yoki vaqtni o'zgartirish kerak bo'lsa, biz bilan bog'laning. 💬\n\n"
                 f"💚 <i>Sog'ligingiz bizning ustuvor vazifamiz!</i> �",
            parse_mode="HTML"
        )
