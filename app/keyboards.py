from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Upload'),
        KeyboardButton(text='Select')
    ],
    [
        KeyboardButton(text='Use')
    ]
],
    resize_keyboard=True,
    input_field_placeholder='Choose menu point')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='First model(linear regression)', url='https://youtube.com')
    ]
])