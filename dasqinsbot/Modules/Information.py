from pyrogram import filters
from pyrogram import Client as dasqinsbot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant
from dasqinsbot.Translation import Translation
from dasqinsbot.Config import Config
from dasqinsbot.Modules.Buttons import ID_BUTTON, INFO_BUTTON

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

@dasqinsbot.on_message(filters.private & filters.command("id"))
async def id_handler(dasqin, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await dasqin.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("Ba???la, S?n **Ban oldun ?**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From dasqin.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  

    reply_markup = ID_BUTTON
    await update.reply_text(        
        text=Translation.ID_TEXT.format(update.from_user.id),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@dasqinsbot.on_message(filters.private & filters.command("info"))
async def info_handler(dasqin, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await dasqin.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("Ba???la, S?n**Ban oldun ?**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From dasqin.py
            await update.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  

    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "𝐍𝐨𝐧𝐞😔"

    reply_markup = INFO_BUTTON 
    await update.reply_text(  
        text=Translation.INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),             
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
