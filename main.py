import asyncio

from aiogram import Bot,Dispatcher,F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import CommandStart
from keyboards import get_start_kb, get_inline_kb

bot = Bot(token='8200360038:AAE3Qsa8PY4IaE64YexI4S9Iu5TKTBcghRg')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    #Одно сообщение одно клавиатура await message.answer("Чек", reply_markup=ReplyKeyboardRemove())
    await message.answer("привет я шутник", reply_markup=get_start_kb())

# @dp.message(F.text=="чихуахуа")
# async def button1_handler(message: Message):
# #     await message.answer_photo(
# #         "https://pochemychki.com.ua/wp-content/uploads/2024/11/6-1-1.webp",
# #         caption="чихуахуа"
# #     )
# #
# # @dp.message(F.text=="кошка")
# # async def button2_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSU7j0qsOe2ESCuYomWJKbfBvehki-o3nY6rw&s",
# #         caption="кошка"
# #     )
# #
# # @dp.message(F.text=="корова")
# # async def button3_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY6IcujqstFJj9V_wkZAT1jVnzr8BA7t6pdg&s",
# #         caption="корова"
# #     )
# #
# # @dp.message(F.text=="змея")
# # async def button4_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_NigSFefGTEhHqZHGskxvDR7pon3T03PVrw&s",
# #         caption="змея"
# #     )
# #
# # @dp.message(F.text=="хомяк")
# # async def button5_handler(message: Message):
# #     await message.answer_photo(
# #         "https://icdn.lenta.ru/images/2024/03/18/12/20240318124428151/square_1280_828947c85a8838d217fe9fcc8b0a17ec.jpg",
# #         caption="хомяк"
# #     )
# #
# # @dp.message(F.text=="тигр(мой братуха)")
# # async def button6_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo7BPfi4Fv9Fk3ZjeGbcP-Rra9CqB1JVAp_g&s",
# #         caption="тигр(мой братуха)"
# #     )
# #
# # @dp.message(F.text=="медведь")
# # async def button7_handler(message: Message):
# #     await message.answer_photo(
# #         "https://redbook.burpriroda.ru/upload/iblock/e08/rt83kafiaasr36pnttk8dgrdkt687n0h/map_016.jpg",
# #         caption="медведь"
# #     )
# #
# # @dp.message(F.text=="баран")
# # async def button8_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-bWDnzILZNxiUU3We-Cys0s7n4p2elDasLw&s",
# #         caption="баран"
# #     )
# #
# # @dp.message(F.text=="белка")
# # async def button9_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpBDwR2lmPi88NCD7MdYB8rLu4lZgfIlFSbg&s",
# #         caption="белка"
# #     )
# #
# # @dp.message(F.text=="волк")
# # async def button10_handler(message: Message):
# #     await message.answer_photo(
# #         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQrA3atb4croKxbmP9OMi1o7PNJNaBYS0LGA&s",
# #         caption="волк"
# #     )


@dp.message(F.location)
async def location_handler(message: Message):
    await message.answer(
        f"{message.location.latitude}, {message.location.longitude}",
    )

@dp.message(F.contact)
async def contact_handler(message: Message):
    await message.answer(
        f"{message.contact.first_name}, {message.contact.last_name if message.contact.last_name else 'XXX' }\n {message.contact.phone_number}",
    )

@dp.message(F.text == "обычная кнопка")
async def button_handler(message: Message):
    await message.answer("Чек", reply_markup=ReplyKeyboardRemove())
    await message.answer("Выберите действие", reply_markup=get_inline_kb())

@dp.callback_query(F.data == "Jaxangir")
async def cb_handler(cb : CallbackQuery):
    print(cb)
    print(cb.message.text)
    print(cb.data)
    await cb.answer("Привет")
    await cb.message.answer("Hello")

async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())