from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Catalog'),
        KeyboardButton(text='Korzina')
    ],
    [
        KeyboardButton(text='Goods')
    ]
],
    resize_keyboard=True,
    input_field_placeholder='Choose menu point')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='YouTube', url='https://youtube.com')
    ]
])