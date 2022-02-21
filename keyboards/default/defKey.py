from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А4 Rangsiz'),
            KeyboardButton(text='А4 Rangli'),
        ],
    ],
    resize_keyboard=True
)
atmen=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bekor qilish❌'),
        ],
    ],
    resize_keyboard=True
)

