import asyncio
import sqlite3

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InputFile, FSInputFile
from aiogram import types

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


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
    await message.answer("Оберіть номер:", reply_markup=rooms_and_main_kb.as_markup(resize_keyboard=True, input_field_placeholder='Який номер Вас цікавить?'))


@dp.message(F.text == "😐 Стандарт")
async def show_info_by_standard_room(message: types.Message, state: FSMContext):
    await message.answer(f"Оберіть тип кімнати", reply_markup=standard.as_markup(resize_keyboard=True))
    # await state.set_state(BookingState.waiting_for_room_type)


@dp.callback_query(lambda query: query.data == 'one_room_standard')
async def one_room_standard(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/standard1.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 400 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати", reply_markup=standard.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.callback_query(lambda query: query.data == 'two_room_standard')
async def two_room_standard(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/standard2.jpg')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 600 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати", reply_markup=standard.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.message(F.text == "😁 Комфорт")
async def show_info_by_comfort(message: types.Message):
    await message.answer(f"Оберіть тип кімнати", reply_markup=comfort.as_markup(resize_keyboard=True))


@dp.callback_query(lambda query: query.data == 'one_room_comfort')
async def one_room_comfort(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/comfort1.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 500 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати", reply_markup=comfort.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.callback_query(lambda query: query.data == 'two_room_comfort')
async def two_room_comfort(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/comfort2.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 700 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати", reply_markup=comfort.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.message(F.text == "😎 Люкс")
async def show_info_by_luxe(message: types.Message):
    await message.answer(f"Оберіть тип кімнати", reply_markup=luxe.as_markup(resize_keyboard=True))


@dp.callback_query(lambda query: query.data == 'one_room_luxe')
async def one_room_luxe(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/luxe1.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 700 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати", reply_markup=luxe.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.callback_query(lambda query: query.data == 'two_room_luxe')
async def two_room_luxe(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/luxe2.jpg')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 900 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати", reply_markup=luxe.as_markup(resize_keyboard=True))
    await callback.answer()


class BookingState(StatesGroup):
    waiting_for_room_type = State()
    # waiting_one_or_two_room_type = State()
    waiting_for_checkin_date = State()
    waiting_for_checkout_date = State()


@dp.message(F.text == "Забронювати номер")
async def start_booking(message: types.Message, state: FSMContext):
    await state.set_state(BookingState.waiting_for_room_type)
    await message.answer("Для початку бронювання оберіть тип номера:", reply_markup=rooms_kb.as_markup(resize_keyboard=True))


# @dp.message(BookingState.waiting_for_room_type)
# async def process_room_type(message: types.Message, state: FSMContext):
#     one_or_two_room_type = message.text
#     await state.update_data(room_type=one_or_two_room_type)
#     await state.set_state(BookingState.waiting_one_or_two_room_type)
#     await message.answer("Одномісна чи Двомісна?:", reply_markup=one_or_two_rooms_kb.as_markup(resize_keyboard=True))


@dp.message(BookingState.waiting_for_room_type)
async def process_room_type(message: types.Message, state: FSMContext):
    room_type = message.text
    await state.update_data(room_type=room_type)
    await state.set_state(BookingState.waiting_for_checkin_date)
    await message.answer("Введіть дату заїзду (у форматі YYYY-MM-DD):", reply_markup=del_kbd)


@dp.message(BookingState.waiting_for_checkin_date)
async def process_checkin_date(message: types.Message, state: FSMContext):
    checkin_date = message.text
    await state.update_data(checkin_date=checkin_date)
    await state.set_state(BookingState.waiting_for_checkout_date)
    await message.answer("Введіть дату виїзду (у форматі YYYY-MM-DD):")


@dp.message(BookingState.waiting_for_checkout_date)
async def process_checkout_date(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    room_type = data.get('room_type')
    # one_or_two_room_type = data.get('one_or_two_room_type')
    checkin_date = data.get('checkin_date')
    checkout_date = message.text
    # print(room_type + ' ' + one_or_two_room_type + ' ' + checkin_date + ' ' + checkout_date)
    print(room_type + ' ' + checkin_date + ' ' + checkout_date)

    await message.answer("Ваш номер успішно заброньовано!")


@dp.message(F.text == "◀ На головну")
async def start_field(message: types.Message):
    await message.answer("Оберіть дію:", reply_markup=start_kb)


class FeedbackState(StatesGroup):
    waiting_for_feedback = State()


@dp.message(F.text == "Відгуки")
async def feedbacks(message: types.Message, state: FSMContext):
    await message.answer("Напишіть відгук:")
    await state.set_state(FeedbackState.waiting_for_feedback)


@dp.message(FeedbackState.waiting_for_feedback)
async def send_feedback(message: types.Message):
    data = {'user_text': message.text}

    id_user = message.from_user.id

    conn = sqlite3.connect('feedbacks.db')
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO feedback (user_id, user_text) VALUES ({id_user}, '{data['user_text']}')")
    conn.commit()
    conn.close()

    await message.answer("✅ Дякуємо за ваш відгук ✅", reply_markup=start_kb)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
