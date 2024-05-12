from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from datetime import timedelta


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞 Контактна інформація"),
            KeyboardButton(text="🗺 Місця поруч"),
        ],
        [
            KeyboardButton(text="🏘 Номери"),
            KeyboardButton(text="📖 Бронювання номерів"),
        ],
        [
            KeyboardButton(text="💬 Відгуки"),
        ]
    ],
    resize_keyboard=True,
)

del_kbd = ReplyKeyboardRemove()

cancel_kb = ReplyKeyboardBuilder()
cancel_kb.add(
    KeyboardButton(text="❌Скасувати"),
)
cancel_kb.adjust(1)


rooms_kb = ReplyKeyboardBuilder()
rooms_kb.add(
    KeyboardButton(text="Стандарт"),
    KeyboardButton(text="Комфорт"),
    KeyboardButton(text="Люкс"),
)
rooms_kb.add(*cancel_kb.buttons)
rooms_kb.adjust(3, 1)


rooms_and_main_kb = ReplyKeyboardBuilder()
rooms_and_main_kb.add(
    KeyboardButton(text="😐 Стандарт"),
    KeyboardButton(text="😁 Комфорт"),
    KeyboardButton(text="😎 Люкс"),
    KeyboardButton(text="◀ На головну"),
)
rooms_and_main_kb.adjust(3, 1)


one_or_two_rooms_kb = ReplyKeyboardBuilder()
one_or_two_rooms_kb.add(
    KeyboardButton(text="Одномісна"),
    KeyboardButton(text="Двомісна"),
    *cancel_kb.buttons
)
one_or_two_rooms_kb.adjust(2)


cancel_reservation = ReplyKeyboardBuilder()
cancel_reservation.add(
    KeyboardButton(text="❌ Видалити бронювання"),
)


reservation_kb = ReplyKeyboardBuilder()
reservation_kb.add(
    KeyboardButton(text="🔔 Забронювати номер"),
    KeyboardButton(text="📜 Мої заброньовані номери"),
    KeyboardButton(text="◀ На головну"),
)
reservation_kb.adjust(2, 1, 1)


my_reservation_kb = ReplyKeyboardBuilder()
my_reservation_kb.add(
    KeyboardButton(text="🔔 Забронювати номер"),
    *cancel_reservation.buttons,
    KeyboardButton(text="◀ На головну"),)
my_reservation_kb.adjust(2, 1, 1)


places_nearby = ReplyKeyboardBuilder()
places_nearby.add(
    KeyboardButton(text="💊 Аптеки"),
    KeyboardButton(text="🛞 Шиномонтажі"),
    KeyboardButton(text="🍽️ Ресторани / Піцерії"),
    KeyboardButton(text="🍅 Продуктові магазини"),
    KeyboardButton(text="💈 Перукарні / Барбершопи"),
    KeyboardButton(text="🏰 Місця для відпочинку"),
    KeyboardButton(text="◀ На головну"),
)
places_nearby.adjust(2, 2, 2, 1)


def generate_date_keyboard(checkin_date):
    date_kb = ReplyKeyboardBuilder()
    for i in range(8):
        date = checkin_date + timedelta(days=i+1)
        date_kb.add(KeyboardButton(text=f"{date.strftime('%d-%m-%Y')}"))
    date_kb.add(*cancel_kb.buttons)
    return date_kb.adjust(3, 3, 2).as_markup(resize_keyboard=True)



