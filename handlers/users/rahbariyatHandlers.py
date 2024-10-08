import aiogram
from aiogram import types 
from loader import dp, db, checkUser, sendRegText
from .regionHanders import bottomText
from keyboards.inline.rahbariyatKeys import rahbariyatKeys, DDGKeys
from aiogram.types import InputMediaPhoto

@dp.message_handler(text="Сектор раҳбарлари")
async def handleKeys(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply_photo(photo="AgACAgIAAxkBAAINdWR8isQWcNLlZV6_Hy3vyWmlxeSPAAJlyjEbVZToSxRFPcfAPFR9AQADAgADeQADLwQ", caption=f"<b>Исмоилов Серобидин Позилжонович—</b> Избоскан тумани ҳокими, 1-сектор раҳбари \n\n<b>▪️1-сектор штаби:</b> 2-сон Касб-ҳунар мактаби биносида (Собиқ Транспорт коллежи); \n📌Жойлашув- https://maps.app.goo.gl/DkXhsq9s6cv2P62V8 \n\n<b>📩Қабул кунлари:</b> Душанба-шанба кунлари; \n<b>⏰Соат:</b> 9:00 дан 13:00 га қадар; \n<b>📞Телефон номери:</b> +998994386005 \n☎️Штаб номери: +998743122089 \n\n{bottomText}", parse_mode="HTML", reply_markup=rahbariyatKeys)
  else:
    await sendRegText(message)

@dp.callback_query_handler(lambda query: query.data == "sec1Boss")
async def handlerFunc(query: types.CallbackQuery):
  try:
    await query.message.edit_media(InputMediaPhoto(media="AgACAgIAAxkBAAINdWR8isQWcNLlZV6_Hy3vyWmlxeSPAAJlyjEbVZToSxRFPcfAPFR9AQADAgADeQADLwQ", caption=f"<b>Исмоилов Серобидин Позилжонович—</b> Избоскан тумани ҳокими, 1-сектор раҳбари \n\n<b>▪️1-сектор штаби:</b> 2-сон Касб-ҳунар мактаби биносида (Собиқ Транспорт коллежи); \n📌Жойлашув- https://maps.app.goo.gl/DkXhsq9s6cv2P62V8 \n\n<b>📩Қабул кунлари:</b> Душанба-шанба кунлари; \n<b>⏰Соат:</b> 9:00 дан 13:00 га қадар; \n<b>📞Телефон номери:</b> +998994386005 \n☎️Штаб номери: +998743122089 \n\n{bottomText}", parse_mode="HTML"), reply_markup=rahbariyatKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "sec2Boss")
async def handlerFunc(query: types.CallbackQuery):
  try:
    await query.message.edit_media(InputMediaPhoto(media="AgACAgIAAxkBAAINdmR8iy3qPWGsdKX0uTDiWbUxqoSvAAJyyjEbVZToSyF2T5zgx4kqAQADAgADeQADLwQ", caption=f"<b>Каримов Бекмуроджон Анваржонович—</b> Избоскан тумани Прокурори, 2-сектор раҳбари \n\n<b>▪️2-сектор штаби:</b> 7-умумий ўрта таълим мактаби биносида (Бештерак маҳалла фуқаролар йиғини); \n📌Жойлашув- https://maps.app.goo.gl/4CKNDDFyi76Hnks16 \n\n<b>📩Қабул кунлари:</b> Душанба-шанба кунлари; \n<b>⏰Соат:</b> 9:00 дан 13:00 га қадар; \n<b>📞Телефон номери:</b> +998332727001 \n☎️Штаб номери: +998742379946 \n\n{bottomText}", parse_mode="HTML"), reply_markup=rahbariyatKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "sec3Boss")
async def handlerFunc(query: types.CallbackQuery):
  try:
    await query.message.edit_media(InputMediaPhoto(media="AgACAgIAAxkBAAINd2R8i4F6-ExwRN_DdosJuPmU3QJ7AAJkyjEbVZToSyMsgrRCfgNsAQADAgADeQADLwQ", caption=f"<b>Болтаев Муроджон Баходирович—</b> Избоскан тумани Ички ишлар бўлими бошлиғи, 3-сектор раҳбари \n\n<b>▪️3-сектор штаби:</b> Агросаноат теҳникуми биносида (Тинчлик маҳалла фуқаролар йиғини); \n📌Жойлашув- https://maps.app.goo.gl/gzSrW6Ckc4egGPj86 \n\n<b>📩Қабул кунлари:</b> Душанба-шанба кунлари; \n<b>⏰Соат:</b> 9:00 дан 13:00 га қадар; \n<b>📞Телефон номери:</b> +998914821001 \n☎️Штаб номери: +998743124012 \n\n{bottomText}", parse_mode="HTML"), reply_markup=rahbariyatKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "sec4Boss")
async def handlerFunc(query: types.CallbackQuery):
  try:
    await query.message.edit_media(InputMediaPhoto(media="AgACAgIAAxkBAAINeGR8i6Jd6lSVyJd3cYlqB6_8HZUmAAKByjEbVZToS0s71K_gIX0kAQADAgADeQADLwQ", caption=f"<b>Мирзаев Мирзоҳид Асқарович—</b> Избоскан тумани Солиқ инспекцияси бошлиғи, 4-сектор раҳбари \n\n<b>▪️4-сектор штаби:</b> Избоскан туман Солиқ инспекцияси биносида (Қашқарлик маҳалла фуқаролар йиғини); \n📌Жойлашув- https://goo.gl/maps/SgTwicc6NPEhZ43z9 \n\n<b>📩Қабул кунлари:</b> Душанба-шанба кунлари; \n<b>⏰Соат:</b> 9:00 дан 13:00 га қадар; \n<b>📞Телефон номери:</b> +998902084488 \n☎️Штаб номери: +998743124788 \n\n{bottomText}", parse_mode="HTML"), reply_markup=rahbariyatKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.message_handler(text="Туман ҳокимининг ўринбосарлари")
async def handleKeys(message: types.Message):
  inDB = await checkUser(db, message)
  if inDB:
    await message.reply_photo(photo="AgACAgIAAxkBAAINimR8j1wgNGT-pR_IUSxCuo2RVKW3AAKJyjEbVZToS1QDoSY78SXSAQADAgADeQADLwQ", caption=f"👉Умаров Хожиакбар Зафаржон ўғли—Туман ҳокимининг иқтисодиёт ва камбағалликни қисқартириш масалалари бўйича биринчи ўринбосари \n\n📩Қабул кунлари: Ҳафтанинг шанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998981906005 \n\n{bottomText}", parse_mode="HTML", reply_markup=DDGKeys)
  else:
    await sendRegText(message)

@dp.callback_query_handler(lambda query: query.data == "ddg1")
async def handlerFunc(query: types.CallbackQuery):
  try:
    await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINimR8j1wgNGT-pR_IUSxCuo2RVKW3AAKJyjEbVZToS1QDoSY78SXSAQADAgADeQADLwQ", caption=f"👉Умаров Хожиакбар Зафаржон ўғли—Туман ҳокимининг иқтисодиёт ва камбағалликни қисқартириш масалалари бўйича биринчи ўринбосари \n\n📩Қабул кунлари: Ҳафтанинг шанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998981906005 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "ddg2")
async def handlerFunc(query: types.CallbackQuery):
  try:
    await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINi2R8j3in_9JNmRjB7VvrJRCpixKCAAKVyjEbVZToS9qWAxEQlMkTAQADAgADeAADLwQ", caption=f"👉Қамбаров Баҳодир Қодиржонович—Туман ҳокимнинг қурилиш коммуникациялар, комунал хўжалик, экология ва кўкаламзорлаштириш масалалари бўйича ўринбосари \n\n📩Қабул кунлари: Ҳафтанинг пайшанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998950815999 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)    
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "ddg3")
async def handlerFunc(query: types.CallbackQuery):
  try:
      await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINjGR8j6gR9mNjR3x8DfwXZd_kaj4vAAKYyjEbVZToS4B1rhNut7yrAQADAgADeQADLwQ", caption=f"👉Мамажонов Алижон Абдуллаевич—Туман ҳокимнинг ёшлар сиёсати, ижтимоий ривожлантириш ва маънавий-маърифий ишлар масалалари бўйича ўринбосари \n\n📩Қабул кунлари: Ҳафтанинг душанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998998782447 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "ddg4")
async def handlerFunc(query: types.CallbackQuery):
  try:
      await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINjWR8j8bitTQ6yT21eYEUAAE3dQTC_wACnMoxG1WU6EvT4W1my7ycNwEAAwIAA3kAAy8E", caption=f"👉Қодиров Отабек Юсуфжонович—Туман ҳокимининг қишлоқ ва сув хўжалиги масалалари бўйича ўринбосари \n\n📩Қабул кунлари: Ҳафтанинг чоршанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998901472600 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "ddg5")
async def handlerFunc(query: types.CallbackQuery):
  try:
      await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINjmR8kS0FgyGjfLH3fsG6wLxqEA1GAALpyzEbO8DpSxsN7BNoAAGuLwEAAwIAA3kAAy8E", caption=f"👉Ғозиев Дилшодбек Одилжонович—Туман ҳокимнинг ўринбосари-Инвестиция ва ташқи савдо бўлими бошлиғи \n\n📩Қабул кунлари: Ҳафтанинг пайшанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998984447037 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "ddg6")
async def handlerFunc(query: types.CallbackQuery):
  try:
      await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINj2R8kc1FJebJyPEPrLjjpcpKZRuqAALuyzEbO8DpS0zOkNI6P_JFAQADAgADeAADLwQ", caption=f"👉Қобилова Назирахон Қамардиновна—Туман ҳокимнинг ўринбосари-Оила ва хотин-қизлар бўлими бошлиғи \n\n📩Қабул кунлари: Ҳафтанинг сешанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998994720835 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass

@dp.callback_query_handler(lambda query: query.data == "ddg7")
async def handlerFunc(query: types.CallbackQuery):
  try:
      await query.message.edit_media(InputMediaPhoto("AgACAgIAAxkBAAINpWR8kl5t7Ve9c1X3YpzIZmaA2ddjAALyyzEbO8DpS6O-QQmxqN9JAQADAgADeQADLwQ", caption=f"👉Абдусаломова Саидахон Маннабовна—Избоскан тумани Камбағалликни қисқартириш ва бандлик бўлими бошлиғи  \n\n📩Қабул кунлари: Ҳафтанинг сешанба куни; \n⏰Соат: 9:00 дан 12:00 га қадар; \n☎️Телефон: +998993293010 \n\n{bottomText}", parse_mode="HTML"), reply_markup=DDGKeys)
  except aiogram.utils.exceptions.MessageNotModified:
    pass
