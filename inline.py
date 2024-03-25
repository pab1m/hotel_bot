from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_callback_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboard.adjust(*sizes).as_markup()


def get_url_btns(
        *,
        btns: dict[str, str],
        sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    for text, url in btns.items():
        keyboard.add(InlineKeyboardButton(text=text, url=url))

    return keyboard.adjust(*sizes).as_markup()


standard = InlineKeyboardBuilder()
standard.add(InlineKeyboardButton(text="Одномісна", callback_data="one_room_standard"),
             InlineKeyboardButton(text="Двомісна", callback_data="two_room_standard"))

comfort = InlineKeyboardBuilder()
comfort.add(InlineKeyboardButton(text="Одномісна", callback_data="one_room_comfort"),
            InlineKeyboardButton(text="Двомісна", callback_data="two_room_comfort"))

luxe = InlineKeyboardBuilder()
luxe.add(InlineKeyboardButton(text="Одномісна", callback_data="one_room_luxe"),
         InlineKeyboardButton(text="Двомісна", callback_data="two_room_luxe"))
