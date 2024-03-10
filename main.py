import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

from kbds import *
from inline import *


TOKEN = "6822014885:AAGfBcgj1HZeA2BJ1LlFIg76bWhh0gzWQzM"

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):

    phone_number_1 = "+380978237197"
    phone_number_2 = "+380978237197"

    await message.answer(
        f"Вітаю, <b>{message.from_user.full_name}</b>, я Телеграм-бот, який допоможе Вам ознайомитися із готелем "
        f"'Україна'!", parse_mode="html", reply_markup=start_kb)


@dp.message(F.text == "Контактна інформація")
async def contact_info(message: types.Message):
    phone_number_1 = "+380978237197"
    phone_number_2 = "+380978237197"

    # keyboard = types.InlineKeyboardMarkup(row_width=2)
    # keyboard.add(
    #     types.InlineKeyboardButton(text="Зателефонувати 1", url=f"tel:{phone_number_1}"),
    #     types.InlineKeyboardButton(text="Зателефонувати 2", url=f"tel:{phone_number_2}")
    # )
    # keyboard.adjust(2)

    # keyboard = types.InlineKeyboardMarkup(row_width=2)
    # keyboard.add(
    #     types.InlineKeyboardButton(text="Button 1", callback_data="button1"),
    #     types.InlineKeyboardButton(text="Button 2", callback_data="button2")
    # )

    website_url = "https://zlmr.gov.ua/index.php/zhkh/komunalni-pidpryiemstva/hotel-ukraina"
    await message.answer(f"━━━━━<b>Готель 'Україна'</b>━━━━━\n"
                         f"📅Графік роботи: цілодобово\n"
                         f"🌐Вебсайт: <a href='{website_url}'> Комунальне підприємство готель 'Україна' </a>\n"
                         f"📞Телефон для зв'язку 1: {phone_number_1}\n"
                         f"📞Телефон для зв'язку 2: {phone_number_2}\n"
                         f"📧Електронна пошта: <a type='email'>hotel.zl@ukr.net</a>\n"
                         f"👨🏫Керівник:  Гавришків Ірена Петрівна\n"
                         f"🏠Загальна кількість номерного фонду: 18 номерів (36 місць)\n"
                         f"📍Адреса: 80700 Львівська обл. Золочівський р-н, м. Золочів вул. Валова 4\n",
                         parse_mode="html")


    # phone_link_1 = f"Телефон для зв'язку 1: 0673406322"
    # phone_link_2 = f"Телефон для зв'язку 2: 0326542142"
    # website_url = "https://zlmr.gov.ua/index.php/zhkh/komunalni-pidpryiemstva/hotel-ukraina"
    # await message.answer(f"━━━━━<b>Готель 'Україна'</b>━━━━━\n"
    #                      f"📅Графік роботи: цілодобово\n"
    #                      f"🌐Вебсайт: <a href='{website_url}'> Комунальне підприємство готель 'Україна' </a>\n"
    #                      f"📞{phone_link_1}\n"
    #                      f"📞{phone_link_2}\n"
    #                      f"📧Електронна пошта: <a type='email'>hotel.zl@ukr.net</a>\n"
    #                      f"👨🏫Керівник:  Гавришків Ірена Петрівна\n"
    #                      f"🏠Загальна кількість номерного фонду: 18 номерів (36 місць)\n"
    #                      f"📍Адреса: 80700 Львівська обл. Золочівський р-н, м. Золочів вул. Валова 4\n",
    #                      parse_mode="html")


@dp.message(F.text == "Номери")
async def rooms(message: types.Message):
    await message.answer("Оберіть номер:", reply_markup=rooms_kb.as_markup(resize_keyboard=True, input_field_placeholder='Яка номер Вас цікавить?'))


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
