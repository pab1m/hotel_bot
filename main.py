import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InputFile, FSInputFile

from kbds import *
from inline import *


TOKEN = "6822014885:AAGfBcgj1HZeA2BJ1LlFIg76bWhh0gzWQzM"

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        f"Вітаю, <b>{message.from_user.full_name}</b>, я Телеграм-бот, який допоможе Вам ознайомитися із готелем "
        f"'Україна'!", parse_mode="html", reply_markup=start_kb)


@dp.message(F.text == "Контактна інформація")
async def contact_info(message: types.Message):
    phone_link_1 = f"Телефон для зв'язку 1: +380673406322"
    phone_link_2 = f"Телефон для зв'язку 2: +380326542142"
    website_url = "https://zlmr.gov.ua/index.php/zhkh/komunalni-pidpryiemstva/hotel-ukraina"
    map_location = ("https://www.google.com/maps/place/%D0%9A%D0%9F+%D0%B3%D0%BE%D1%82%D0%B5%D0%BB%D1%8C+%C2%AB%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0%C2%BB/@49.8055415,"
                    "24.8994852,18.75z/data=!4m9!3m8!1s0x47300759c6464e6b:0x5a8e1f2257f61a24!5m2!4m1!1i2!8m2!3d49.8055267!4d24.8997192!16s%2Fg%2F11h4rv8b3y?authuser=0&entry=ttu")

    contact_info_keyboard = InlineKeyboardBuilder()
    contact_info_keyboard.add(InlineKeyboardButton(text="🌐Відвідати сайт", url=website_url),
                              InlineKeyboardButton(text="📍На карті", url=map_location))

    await message.answer(f"━━━━━<b>Готель 'Україна'</b>━━━━━\n"
                         f"📅Графік роботи: <b>цілодобово</b>\n\n"
                         
                         f"📞{phone_link_1}\n"
                         f"📞{phone_link_2}\n"
                         f"📧Електронна пошта: <a type='email'>hotel.zl@ukr.net</a>\n\n"
                         
                         f"👨🏫Керівник:  Гавришків Ірена Петрівна\n\n"
                         
                         f"📍Адреса: 80700 Львівська обл. Золочівський р-н, м. Золочів вул. Валова 4\n",
                         parse_mode="html", reply_markup=contact_info_keyboard.as_markup(resize_keyboard=True)
            #              get_url_btns(
            # btns={
            #     '🌐Відвідати сайт': f'{website_url}',
            #     '📍На карті': f'{map_location}'
            # })
    )


@dp.message(F.text == "Номери")
async def rooms(message: types.Message):
    await message.answer(f"🏠Загальна кількість номерного фонду: 18 номерів (36 місць)\n")
    await message.answer("Оберіть номер:", reply_markup=rooms_kb.as_markup(resize_keyboard=True, input_field_placeholder='Яка номер Вас цікавить?'))


@dp.message(F.text == "😐 Звичайний")
async def show_info_by_room1(message: types.Message):
    # with open("rooms_photo/default.jpg", 'rb') as room:
    #     await bot.send_photo(chat_id=message.from_user.id, photo=room)

    photo = FSInputFile(r'rooms_photo/default.jpg')
    await bot.send_photo(message.chat.id, photo)
    await message.answer(f"🏠Загальна кількість номерного фонду: 18 номерів (36 місць)\n")
        # await message.answer("Оберіть номер:", reply_markup=rooms_kb.as_markup(resize_keyboard=True, input_field_placeholder='Яка номер Вас цікавить?'))


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
