from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from datetime import datetime, timedelta


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📜 Контактна інформація"),
        ],
        [
            KeyboardButton(text="🏘 Номери"),
            KeyboardButton(text="Забронювати номер"),
        ],
        [
            KeyboardButton(text="💬 Відгуки"),
        ]
    ],
    resize_keyboard=True,
)

del_kbd = ReplyKeyboardRemove()


rooms_kb = ReplyKeyboardBuilder()
rooms_kb.add(
    KeyboardButton(text="Стандарт"),
    KeyboardButton(text="Комфорт"),
    KeyboardButton(text="Люкс"),
)
rooms_kb.adjust(2, 1)


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
)
one_or_two_rooms_kb.adjust(2)


def generate_date_keyboard(checkin_date):
    date_kb = ReplyKeyboardBuilder()
    for i in range(8):
        date = checkin_date + timedelta(days=i+1)
        date_kb.add(KeyboardButton(text=f"{date.strftime('%d-%m-%Y')}"))
    return date_kb.adjust(3, 3, 2).as_markup(resize_keyboard=True)



