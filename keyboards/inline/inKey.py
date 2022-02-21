from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
menyuin = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Ha", callback_data="xa"),
        InlineKeyboardButton(text="Yo'q", callback_data="yoq"),
    ],
])