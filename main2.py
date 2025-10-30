import asyncio

from aiogram import Bot,Dispatcher,F
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart
from keyboards import get_start_kb, get_inline_kb, get_test_kb

bot = Bot(token='8200360038:AAE3Qsa8PY4IaE64YexI4S9Iu5TKTBcghRg')
dp = Dispatcher()
data = {}
@dp.message(CommandStart())
async def start_handler(message: Message):
    #Одно сообщение одно клавиатура
    data.clear()
    await message.answer("В каком году вторая мировая \nA)1940\nB)1941\nC)1939\nD)1938", reply_markup=get_test_kb(1))

@dp.callback_query(F.data.startswith("test"))
async def test_handler(cb: CallbackQuery):
    _ , number , answer = cb.data.split("_")
        # await cb.message.answer("пон")
    print(cb.data)
    if number == "1":
        data[number] = answer
        await cb.message.edit_text(
            "В каком году закончилась вторая мировая? \nA)1991\nB)1981\nC)1971\nD)1945",
            reply_markup = get_test_kb(2)
        )
    elif number == "2":
        await cb.message.edit_text(
            "Вы прошли тест",
            reply_markup=None
        )
        await cb.message.answer(f"{data}")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())