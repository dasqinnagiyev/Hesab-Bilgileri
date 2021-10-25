from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ID_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 DAQO MODS'A qatıl", url="t.me/dasqin")
       ]]
       )
INFO_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 DAQO MODS'A qatıl", url="t.me/dasqin")
       ]]
       )
ID_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("↗️ Məlumat", callback_data="info")
       ],[
       InlineKeyboardButton("🔙 Yardım'a qayıt", callback_data="yardim")
       ]]
       )
INFO_BUTTONS = InlineKeyboardMarkup( [[
       InlineKeyboardButton("↗️ Telegram ID️", callback_data="id")
       ],[
       InlineKeyboardButton("🔙 Yardım'a qayıt", callback_data="yardim")
       ]]
       )
JSON_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 DAQO MODS'A qatıl", url="t.me/dasqin")
       ]]
       )
