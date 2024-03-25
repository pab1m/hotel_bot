from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Контактна інформація"),
        ],
        [
            KeyboardButton(text="Номери"),
            KeyboardButton(text="Забронювати номер"),
        ],
        [
            KeyboardButton(text="Відгуки"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Що Вам цікаво?'
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


# @dp.message(BookingState.waiting_for_room_type)
# async def process_room_type(message: types.Message, state: FSMContext):
#     one_or_two_room_type = message.text
#     await state.update_data(room_type=one_or_two_room_type)
#     await state.set_state(BookingState.waiting_one_or_two_room_type)
#     await message.answer("Одномісна чи Двомісна?:", reply_markup=one_or_two_rooms_kb.as_markup(resize_keyboard=True))
