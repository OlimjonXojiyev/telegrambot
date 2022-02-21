from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.defKey import menu,atmen
from aiogram.dispatcher import FSMContext
from keyboards.inline.inKey import menyuin
from loader import dp
from aiogram.types import CallbackQuery



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nKerakli bo'limni tanlang👇",reply_markup=menu)
@dp.message_handler(text='Bekor qilish❌',state='*')
async def bot_start(message: types.Message):
    await message.answer(f"Kerakli bo'limni tanlang👇",reply_markup=menu)
@dp.message_handler(text='А4 Rangsiz')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Chiqarmoqchi bo'lgan kitob varoq sonini kiriting👇",reply_markup=atmen)
    await state.set_state('А4 Rangsiz')
@dp.message_handler(state='А4 Rangsiz')
async def bot_start(message: types.Message, state: FSMContext):
    son = message.text
    await state.update_data({'son': son})
    await message.answer(f"\"Переплёт\" kerakmi?",reply_markup=menyuin)
    await state.set_state('prep')
@dp.callback_query_handler(text="xa",state='prep')
async def bot_start(call: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        son = data.get('son')
        varoq=int(son)*200
        varoq1 = int(son) * 200 + 5000
        await call.message.answer(f"{son} varoq uchun <b>{str(varoq)}</b> so'm\n\"Переплёт\" uchun <b>5000</b> so'm\nUmumi: <b>{str(varoq1)}</b> so'm"
                                  f"\n\nChiqarmoqchi bo'lgan kitobni @kopiyakitob ga yuboring oldindan buyurtma qilib qo'ysangiz ham bo'ladi😊",reply_markup=menu)
        await state.finish()
    except ValueError:
        await state.set_state('А4 Rangsiz')
        await call.message.answer("Faqat son ko'rinishida yuboring!")
        await call.message.answer(f"Chiqarmoqchi bo'lgan kitob varoq sonini kiriting👇", reply_markup=atmen)
@dp.callback_query_handler(text="yoq",state='prep')
async def bot_start(call: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        son = data.get('son')
        varoq=int(son)*200
        await call.message.answer(f"{son} varoq uchun <b>{str(varoq)} so'm</b>."
                                  f"\n\nChiqarmoqchi bo'lgan kitobni @kopiyakitob ga yuboring oldindan buyurtma qilib qo'ysangiz ham bo'ladi😊",reply_markup=menu)
        await state.finish()
    except ValueError:
        await state.set_state('А4 Rangsiz')
        await call.message.answer("Faqat son ko'rinishida yuboring!")
        await call.message.answer(f"Chiqarmoqchi bo'lgan kitob varoq sonini kiriting👇", reply_markup=atmen)
############################################################
@dp.message_handler(text='А4 Rangli')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Chiqarmoqchi bo'lgan kitob varoq sonini kiriting👇",reply_markup=atmen)
    await state.set_state('А4 Rangli')
@dp.message_handler(state='А4 Rangli')
async def bot_start(message: types.Message, state: FSMContext):
    son = message.text
    await state.update_data({'son': son})
    await message.answer(f"\"Переплёт\" kerakmi?",reply_markup=menyuin)
    await state.set_state('prep1')
@dp.callback_query_handler(text="xa",state='prep1')
async def bot_start(call: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        son = data.get('son')
        varoq=int(son)*500
        varoq1 = int(son) * 500 + 5000
        await call.message.answer(f"{son} varoq uchun <b>{str(varoq)}</b> so'm\n\"Переплёт\" uchun <b>5000</b> so'm\nUmumi: <b>{str(varoq1)}</b> so'm"
                                  f"\n\nChiqarmoqchi bo'lgan kitobni @kopiyakitob ga yuboring oldindan buyurtma qilib qo'ysangiz ham bo'ladi😊",reply_markup=menu)
        await state.finish()
    except ValueError:
        await state.set_state('А4 Rangli')
        await call.message.answer("Faqat son ko'rinishida yuboring!")
        await call.message.answer(f"Chiqarmoqchi bo'lgan kitob varoq sonini kiriting👇", reply_markup=atmen)
@dp.callback_query_handler(text="yoq",state='prep1')
async def bot_start(call: CallbackQuery, state: FSMContext):
    try:
        data = await state.get_data()
        son = data.get('son')
        varoq=int(son)*500
        await call.message.answer(f"{son} varoq uchun <b>{str(varoq)} so'm</b>."
                                  f"\n\nChiqarmoqchi bo'lgan kitobni @kopiyakitob ga yuboring oldindan buyurtma qilib qo'ysangiz ham bo'ladi😊",reply_markup=menu)
        await state.finish()
    except ValueError:
        await state.set_state('А4 Rangsiz')
        await call.message.answer("Faqat son ko'rinishida yuboring!")
        await call.message.answer(f"Chiqarmoqchi bo'lgan kitob varoq sonini kiriting👇", reply_markup=atmen)





