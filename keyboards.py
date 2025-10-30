from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiohttp import request
from aiogram.types import Message

#ReplyKeyboardMarkup -> каркас клавиатуры(который меняет основную клавиатуру пользователя)

#KeyboardButton -> клавиша клавиатуры
#Он служит чтобы просто упростить ввод текста
# kb = ReplyKeyboardMarkup(
#     keyboard=
#     [
#         [
#         KeyboardButton(
#             text="чихуахуа"
#             ),
#         KeyboardButton(
#             text="кошка"
#         ),
#         ],
#
#
#         [
#         KeyboardButton(
#             text="корова"
#         ),
#         KeyboardButton(
#             text="змея"
#         ),
#         KeyboardButton(
#             text="хомяк"
#         ),
#         ],
#
#
#         [
#         KeyboardButton(
#             text="тигр(мой братуха)"
#         ),
#         ],
#
#
#         [
#         KeyboardButton(
#             text="медведь"
#         ),
#         KeyboardButton(
#             text="баран"
#         ),
#         KeyboardButton(
#             text="белка"
#         ),
#         KeyboardButton(
#             text="волк"
#         ),
#         ],
#     ],
#     resize_keyboard=True
# )


def get_start_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="обычная кнопка",
    )
    builder.button(
        text="Геопозиция",
        request_location=True,
    )
    builder.button(
        text="Контакт",
        request_contact=True,
    )
    builder.adjust(2,1)
    return builder.as_markup(
        resize_keyboard=True,
    )

def get_inline_kb():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="ссылка",
        url="https://it911.uz",
    )
    builder.button(
        text="Дата",
        callback_data="Jaxangir",
    )
    return builder.as_markup()

def get_test_kb(test_number):
    builder = InlineKeyboardBuilder()
    builder.button(
        text="A",
        callback_data=f"test_{test_number}_A",
    ),
    builder.button(
        text="B",
        callback_data=f"test_{test_number}_B",
    ),
    builder.button(
        text="C",
        callback_data=f"test_{test_number}_C",
    ),
    builder.button(
        text="D",
        callback_data=f"test_{test_number}_D",
    ),
    return builder.as_markup()