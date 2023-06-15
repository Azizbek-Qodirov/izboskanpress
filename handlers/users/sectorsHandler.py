from aiogram import types
from loader import dp, db, checkUser, sendRegText
from keyboards.inline.mfys import *

@dp.message_handler(text="Сектор I")
async def sec1(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector1)
  else:
    await sendRegText(message)

@dp.message_handler(text="Сектор II")
async def sec2(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector2)
  else:
    await sendRegText(message)

@dp.message_handler(text="Сектор III")
async def sec3(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector3)
  else:
    await sendRegText(message)

@dp.message_handler(text="Сектор IV")
async def sec4(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply(text="Қуйидаги МФЙлардан бирини танланг: ", reply_markup=sector4)
  else:
    await sendRegText(message)

@dp.message_handler(text="🤖 Онлайн маҳалла бот")
async def sec4(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply(text="Онлайн маҳалла ташкилотининг расмий боти: \n\n@online_mahalla_bot")
  else:
    await sendRegText(message)
