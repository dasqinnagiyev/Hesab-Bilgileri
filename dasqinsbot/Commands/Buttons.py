from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

START_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("📢 DAQO MODS", url=f"t.me/dasqin"),
       InlineKeyboardButton("Instagram'da izlə 💫", url=f"https://instagram.com/dasqinnagiyev")
       ],[
       InlineKeyboardButton("⬇️ Ətraflı məlumat ⬇️", callback_data="yardim")
       ]]
       )

HELP_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Telegram ID", callback_data="id"),
       InlineKeyboardButton("Telegram Info", callback_data="info")
       ],[
       InlineKeyboardButton("🏠 Yenidən başla", callback_data="start"),
       InlineKeyboardButton("⬇️ Bağla", callback_data="bagla"),
       InlineKeyboardButton("🤠 Haqqında", callback_data="haqqinda")
       ]]
       )

ABOUT_BUTTON = InlineKeyboardMarkup( [[
       InlineKeyboardButton("🔙 Geriyə qayıt", callback_data="yardim"),
       InlineKeyboardButton("🏠 Yenidən başla", callback_data="start"),
       InlineKeyboardButton("⬇️ Bağla", callback_data="bagla")
       ]]
       )
