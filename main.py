import asyncio
import sqlite3

from aiogram.filters import StateFilter
from aiogram.types import FSInputFile
from aiogram import types

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from datetime import datetime

from kbds import *
from inline import *

from places import *

TOKEN = "6822014885:AAGfBcgj1HZeA2BJ1LlFIg76bWhh0gzWQzM"

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        f"Вітаю, <b>{message.from_user.full_name}</b>, я Телеграм-бот, "
        f"який допоможе Вам ознайомитися із готелем "
        f"'Україна'!", parse_mode="html", reply_markup=start_kb)


@dp.message(F.text == "📞 Контактна інформація")
async def contact_info(message: types.Message):
    phone_link_1 = f"Телефон для зв'язку 1: +380673406322"
    phone_link_2 = f"Телефон для зв'язку 2: +380326542142"
    website_url = "https://zlmr.gov.ua/index.php/zhkh/komunalni-pidpryiemstva/hotel-ukraina"
    map_location = (
        "https://www.google.com/maps/place/%D0%9A%D0%9F+%D0%B3%D0%BE%D1%82%D0%B5%D0%BB%D1%8C+%C2%AB%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0%C2%BB/@49.8055415,"
        "24.8994852,18.75z/data=!4m9!3m8!1s0x47300759c6464e6b:0x5a8e1f2257f61a24!5m2!4m1!1i2!8m2!3d49.8055267!4d24.8997192!16s%2Fg%2F11h4rv8b3y?authuser=0&entry=ttu")

    contact_info_keyboard = InlineKeyboardBuilder()
    contact_info_keyboard.add(InlineKeyboardButton(text="🌐Відвідати сайт", url=website_url),
                              InlineKeyboardButton(text="📍На карті", url=map_location))

    await message.answer(f'━━━━━<b>Готель "Україна"</b>━━━━━\n'
                         f"📅Графік роботи: <b>цілодобово</b>\n\n"

                         f"📞{phone_link_1}\n"
                         f"📞{phone_link_2}\n"
                         f"📧Електронна пошта: <a type='email'>hotel.zl@ukr.net</a>\n\n"

                         f"👨🏫Керівник:  Гавришків Ірена Петрівна\n\n"

                         f"📍Адреса: 80700 Львівська обл. Золочівський р-н, м. Золочів вул. Валова 4\n",
                         parse_mode="html", reply_markup=contact_info_keyboard.as_markup(resize_keyboard=True))


class FeedbackState(StatesGroup):
    waiting_for_feedback = State()


@dp.message(F.text == "💬 Відгуки")
async def feedbacks(message: types.Message, state: FSMContext):
    await message.answer("Напишіть відгук:", reply_markup=del_kbd)
    await state.set_state(FeedbackState.waiting_for_feedback)


@dp.message(FeedbackState.waiting_for_feedback)
async def send_feedback(message: types.Message, state: FSMContext):
    data = {'user_text': message.text}

    id_user = message.from_user.id

    conn = sqlite3.connect('feedbacks.db')
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO feedback (user_id, user_text) VALUES ({id_user}, '{data['user_text']}')")
    conn.commit()
    conn.close()
    await state.clear()
    await message.answer("✅ Дякуємо за ваш відгук ✅", reply_markup=start_kb)


@dp.message(F.text == "🏘 Номери")
async def rooms(message: types.Message):
    await message.answer(f"🏠Загальна кількість номерного фонду: 18 номерів (36 місць)\n")
    await message.answer("Оберіть номер:", reply_markup=rooms_and_main_kb.as_markup(resize_keyboard=True))


@dp.message(F.text == "😐 Стандарт")
async def show_info_by_standard_room(message: types.Message):
    await message.answer(f"Оберіть тип кімнати:", reply_markup=standard.as_markup(resize_keyboard=True))


@dp.callback_query(lambda query: query.data == 'one_room_standard')
async def one_room_standard(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/standard1.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 400 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати:", reply_markup=standard.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.callback_query(lambda query: query.data == 'two_room_standard')
async def two_room_standard(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/standard2.jpg')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 600 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати:", reply_markup=standard.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.message(F.text == "😁 Комфорт")
async def show_info_by_comfort(message: types.Message):
    await message.answer(f"Оберіть тип кімнати:", reply_markup=comfort.as_markup(resize_keyboard=True))


@dp.callback_query(lambda query: query.data == 'one_room_comfort')
async def one_room_comfort(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/comfort1.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 500 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати:", reply_markup=comfort.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.callback_query(lambda query: query.data == 'two_room_comfort')
async def two_room_comfort(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/comfort2.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 700 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати:", reply_markup=comfort.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.message(F.text == "😎 Люкс")
async def show_info_by_luxe(message: types.Message):
    await message.answer(f"Оберіть тип кімнати:", reply_markup=luxe.as_markup(resize_keyboard=True))


@dp.callback_query(lambda query: query.data == 'one_room_luxe')
async def one_room_luxe(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/luxe1.webp')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 700 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати:", reply_markup=luxe.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.callback_query(lambda query: query.data == 'two_room_luxe')
async def two_room_luxe(callback: types.CallbackQuery):
    photo = FSInputFile(r'rooms_photo/luxe2.jpg')
    await bot.send_photo(callback.message.chat.id, photo)
    await callback.message.answer(f"❗Ціна - 900 грн💸\n")
    await callback.message.answer(f"Оберіть тип кімнати:", reply_markup=luxe.as_markup(resize_keyboard=True))
    await callback.answer()


@dp.message(F.text == "🗺 Місця поруч")
async def place_nearby(message: types.Message):
    await message.answer("Оберіть:", reply_markup=places_nearby.as_markup(resize_keyboard=True))


@dp.message(F.text == "💊 Аптеки")
async def pharmacies(message: types.Message):
    pharmacy_1 = ("Західна Фармацевтична Компанія", "вул. Володимира Івасюка 2", "08:30-21:00", "https://maps.app.goo.gl/zcFBVZwtxUvVcsoS8")
    pharmacy_2 = ("Подорожник", "вул. Василя Пачовського 1", "08:00–18:00", "https://maps.app.goo.gl/rAyYg88zmJY1zqq9A")
    pharmacy_3 = ("Аптека 3і", "вул. Маркіяна Шашкевича 5", "08:00–20:00", "https://maps.app.goo.gl/TLqEi1kRw3vyxkJ66")

    pharmacies_info = place_def(pharmacy_1, pharmacy_2, pharmacy_3)

    await message.answer(pharmacies_info, parse_mode="html")


@dp.message(F.text == "🛞 Шиномонтажі")
async def tire_fitting(message: types.Message):
    tire_fitting_1 = ("Шиномонтаж", "вул. Івана Труша", "09:00–18:00", "https://maps.app.goo.gl/L1PjnCUXd3Jxtja49")
    tire_fitting_2 = ("Redbox", "вул. Бродівська 19", "09:00–19:00", "https://maps.app.goo.gl/PwmNuuhTGWA92Ue8A")
    tire_fitting_3 = ("Шиномонтаж", "вул. Львівська 50", "09:00–18:00", "https://maps.app.goo.gl/sPLhr41LeznSvoKL6")

    tire_fitting_info = place_def(tire_fitting_1, tire_fitting_2, tire_fitting_3)

    await message.answer(tire_fitting_info, parse_mode="html")


@dp.message(F.text == "🍽️ Ресторани / Піцерії")
async def restaurants_and_pizzerias(message: types.Message):
    restaurants_and_pizzerias_1 = ("Пріма-Піца", "вул. Валова 4а", "10:00–22:00", "https://maps.app.goo.gl/vg7YDVGDCp4w42rc8")
    restaurants_and_pizzerias_2 = ("Piccadilly", "вул. Михайла Лермонтова 2а", "09:00–19:00", "https://maps.app.goo.gl/Ac9q9QDnrXuoKfnw5")
    restaurants_and_pizzerias_3 = ("Маяк", "вул. Пушкіна", "11:00–22:00", "https://maps.app.goo.gl/6hEW1DYAZLPBdw239")

    restaurants_and_pizzerias_info = place_def(restaurants_and_pizzerias_1, restaurants_and_pizzerias_2, restaurants_and_pizzerias_3)

    await message.answer(restaurants_and_pizzerias_info, parse_mode="html")


@dp.message(F.text == "🍅 Продуктові магазини")
async def product(message: types.Message):
    product_1 = ("Наш Край", "вул. Січових Стрільців 5", "08:00–22:00", "https://maps.app.goo.gl/aBDppJERnFj1Jnpt6")
    product_2 = ("Гурман", "вул. Січових Стрільців 2Д", "08:00–20:00", "https://maps.app.goo.gl/zHDey7C5qa1wUK6i8")
    product_3 = ("АТБ", "вул. Львівська 5Б", "08:00–23:00", "https://maps.app.goo.gl/oV9yEkcsk7Nn6djYA")

    product_info = place_def(product_1, product_2, product_3)

    await message.answer(product_info, parse_mode="html")


@dp.message(F.text == "💈 Перукарні / Барбершопи")
async def hairdressers(message: types.Message):
    hairdressers_1 = ("Barbershop Scissors", "вул. Львівська 5Б", "10:00–20:00", "https://maps.app.goo.gl/Vvi8ZRqTb6Stm4Tq6")
    hairdressers_2 = ("Barbershop Berserker", "вул. Романа Шухевича 3а", "10:00–21:00", "https://maps.app.goo.gl/a1PSvhYvRAyRJDZY8")
    hairdressers_3 = ("Перукарня «Юля»", "вул. Михайла Лермонтова 2а", "09:00–18:00", "https://maps.app.goo.gl/Erzgew2XYQWhaN9i8")

    hairdressers_info = place_def(hairdressers_1, hairdressers_2, hairdressers_3)

    await message.answer(hairdressers_info, parse_mode="html")


@dp.message(F.text == "🏰 Місця для відпочинку")
async def vacation(message: types.Message):
    vacation_1 = ("Парк імені гетьмана України Самуїла Зборовського", "вул. Валова", "Цілодобово", "https://maps.app.goo.gl/xCUbDUYnD63t9yGy5")
    vacation_2 = ("Золочівський замок", "вул. Тернопільська", "11:00–17:30", "https://maps.app.goo.gl/5Mm983YMuq4zhQdK8")
    vacation_3 = ("Парк «Здоров'я»", "вул. Маркіяна Шашкевича", "Цілодобово", "https://maps.app.goo.gl/QzXmcVcc1jti3Qb18")

    vacation_info = place_def(vacation_1, vacation_2, vacation_3)

    await message.answer(vacation_info, parse_mode="html")


class BookingState(StatesGroup):
    room_type = State()
    one_or_two_room_type = State()
    checkin_date = State()
    checkout_date = State()
    name = State()


@dp.message(F.text == "📖 Бронювання номерів")
async def start_booking(message: types.Message):
    await message.answer("Оберіть:", reply_markup=reservation_kb.as_markup(resize_keyboard=True))


@dp.message(F.text == "🔔 Забронювати номер")
async def booking(message: types.Message, state: FSMContext):
    await message.answer(
        'Для початку бронювання оберіть тип номера: \n(якщо потрібно відмінити всі дії, введіть команду <b>"скасувати"</b>)',
        reply_markup=rooms_kb.as_markup(resize_keyboard=True), parse_mode='html')
    await state.set_state(BookingState.room_type)


@dp.message(StateFilter('*'), Command("скасувати"))
@dp.message(StateFilter('*'), F.text.casefold() == "скасувати")
@dp.message(StateFilter('*'), F.text == "❌Скасувати")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer("❗Дія скасована❗", reply_markup=reservation_kb.as_markup(resize_keyboard=True))


@dp.message(BookingState.room_type)
async def one_or_two_rooms_type(message: types.Message, state: FSMContext):
    room_type = message.text
    if room_type in ["Стандарт", "Комфорт", "Люкс"]:
        await state.update_data(room_type=room_type)
        await message.answer("Одномісна чи Двомісна?", reply_markup=one_or_two_rooms_kb.as_markup(resize_keyboard=True))
        await state.set_state(BookingState.one_or_two_room_type)
    else:
        await message.answer("Будь ласка, оберіть номер зі списку.", reply_markup=rooms_kb.as_markup(resize_keyboard=True))


@dp.message(BookingState.one_or_two_room_type)
async def checkin_dates(message: types.Message, state: FSMContext):
    one_or_two_room_type = message.text
    if one_or_two_room_type in ["Одномісна", "Двомісна"]:
        await state.update_data(one_or_two_room_type=one_or_two_room_type)
        await message.answer("Оберіть дату заїзду:", reply_markup=generate_date_keyboard(datetime.now().date().today()))
        await state.set_state(BookingState.checkin_date)
    else:
        await message.answer("Будь ласка, оберіть тип із списку.", reply_markup=one_or_two_rooms_kb.as_markup(resize_keyboard=True))


@dp.message(BookingState.checkin_date)
async def checkout_dates(message: types.Message, state: FSMContext):
    try:
        checkin_date = datetime.strptime(message.text, "%d-%m-%Y").date()
        await state.update_data(checkin_date=checkin_date)
        await message.answer("Оберіть дату виїзду:", reply_markup=generate_date_keyboard(checkin_date))
        await state.set_state(BookingState.checkout_date)
    except ValueError:
        await message.answer("Будь ласка, оберіть дату із запропонованих.")


@dp.message(BookingState.checkout_date)
async def process_checkin_inf(message: types.Message, state: FSMContext):
    try:
        await state.update_data(checkout_date=datetime.strptime(message.text, "%d-%m-%Y").date())
        await message.answer("Введіть <b>Прізвище</b> та <b>Ім'я</b>", parse_mode="html", reply_markup=del_kbd)
        await state.set_state(BookingState.name)
    except ValueError:
        await message.answer("Будь ласка, введіть коректні дані.")


@dp.message(BookingState.name)
async def process_checkout_date(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id_user = message.from_user.id
    room_type = data.get('room_type')
    one_or_two_room_type = data.get('one_or_two_room_type')
    checkin_date = data.get('checkin_date')
    checkout_date = data.get('checkout_date')

    inf = message.text
    inf_parts = inf.split()
    first_name = inf_parts[0]
    last_name = ' '.join(inf_parts[1:])

    conn = sqlite3.connect('reservation.db')
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO reservation (user_id, room_type, one_or_two_room_type, checkin_date, checkout_date, first_name, last_name)"
        f" VALUES ({id_user}, '{room_type}', '{one_or_two_room_type}', '{checkin_date}', '{checkout_date}', '{first_name}', '{last_name}')")
    conn.commit()
    conn.close()

    await state.clear()
    await message.answer("✅ Ваш номер успішно заброньовано! ✅", reply_markup=start_kb)
    await state.clear()


@dp.message(F.text == "📜 Мої заброньовані номери")
async def my_bookings(message: types.Message):
    user_id = message.from_user.id

    conn = sqlite3.connect('reservation.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM reservation WHERE user_id = {user_id}")
    reservations = cursor.fetchall()
    conn.close()

    if not reservations:
        await message.answer("У вас немає заброньованих номерів.")
        return

    response = "Ваші заброньовані номери:\n"
    await message.answer(response, reply_markup=my_reservation_kb.as_markup(resize_keyboard=True))

    for reservation in reservations:
        response = (f"\n✅ ID Вашого бронювання: <b>{reservation[0]}</b>"
                    f"\n🏠 Тип номера: <b>{reservation[2]}</b> "
                    f"\n🛏 Одно-/двомісна: <b>{reservation[3]}</b> "
                    f"\n🗓 Дата заїзду: <b>{reservation[4]}</b> "
                    f"\n📆 Дата виїзду: <b>{reservation[5]}</b>\n")
        await message.answer(response, parse_mode="html")


@dp.message(lambda message: message.text.startswith("❌ Видалити бронювання"))
async def cancel_reservation(message: types.Message):
    user_id = message.from_user.id
    conn = sqlite3.connect('reservation.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM reservation WHERE user_id = {user_id}")
    remaining_reservations = cursor.fetchall()
    if not remaining_reservations:
        await message.answer("У вас не залишилося жодного бронювання.")
    else:
        await message.answer("Введіть ID бронювання:", reply_markup=del_kbd)

        @dp.message(lambda msg: msg.from_user.id == user_id)
        async def process_reservation_id(msg: types.Message):
            try:
                reservation_id = int(msg.text)
            except ValueError:
                await message.answer("Неправильний формат ID. Будь ласка, введіть ціле число.")
                return

            cursor.execute(f"SELECT * FROM reservation WHERE id = {reservation_id} AND user_id = {user_id}")
            reservation = cursor.fetchone()

            if reservation:
                cursor.execute(f"DELETE FROM reservation WHERE id = {reservation_id}")
                conn.commit()
                await message.answer(f"Бронювання <b>{reservation_id}</b> видалено.", reply_markup=reservation_kb.as_markup(resize_keyboard=True), parse_mode='html')
            else:
                await message.answer("Це не ваше бронювання, видалення неможливе.", reply_markup=reservation_kb.as_markup(resize_keyboard=True))
    # conn.close()


@dp.message(F.text == "◀ На головну")
async def start_field(message: types.Message):
    await message.answer("Оберіть дію:", reply_markup=start_kb)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
