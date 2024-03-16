from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Контактна інформація"),
        ],
        [
            KeyboardButton(text="Номери"),
            KeyboardButton(text="Відгуки"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Що Вам цікаво?'
)

del_kbd = ReplyKeyboardRemove()


rooms_kb = ReplyKeyboardBuilder()
rooms_kb.add(
    KeyboardButton(text="😐 Стандарт"),
    KeyboardButton(text="😁 Комфорт"),
    KeyboardButton(text="😎 Люкс"),
    KeyboardButton(text="◀ На головну"),
)
rooms_kb.adjust(3, 1)


# rooms_1_or_2 = ReplyKeyboardBuilder()
# rooms_1_or_2.add(
#     KeyboardButton(text="Однокімнатна"),
#     KeyboardButton(text="Двокімнатна"),
#     KeyboardButton(text="Номери"),
# )
# rooms_1_or_2.adjust(2, 1)

