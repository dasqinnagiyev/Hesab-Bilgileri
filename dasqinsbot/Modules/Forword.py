from pyrogram import filters
from pyrogram import Client as dasqinsbot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from dasqinsbot.Translation import Translation
from dasqinsbot.Config import Config

UPDATE_CHANNEL=Config.UPDATE_CHANNEL # Update Channel Forces Subscribe
BOT_USERNAME=Config.BOT_USERNAME # ReStart Option 
JOIN=Translation.JOIN_TEXT # Button Text (Update Channel)
TRY=Translation.TRY_TEXT # Button Text (Update Channel)
SUB_TEXT=Translation.FSUB_TEXT # FSUB Information Text

@dasqinsbot.on_message(filters.private & filters.forwarded)
async def info(dasqin, msg):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await dasqin.get_chat_member(update_channel, msg.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Bağışla, Sən **Ban oldun 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From dasqin.py
            await msg.reply_text(
                text=f"<b>{SUB_TEXT}</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=f"{JOIN}", url=f"t.me/{UPDATE_CHANNEL}")],
                    [ InlineKeyboardButton(text=f"{TRY}", url=f"https://t.me/{BOT_USERNAME}?start=try")]
              ])
            )
            return
        except Exception:
            await msg.reply_text(f"@{UPDATE_CHANNEL}")
            return
    if msg.forward_from:
        text = "<u>İlətilən (forward) Mesaj Məlumatları 👀</u> \n\n"
        if msg.forward_from["is_bot"]:
            text += "<u>🤖 Bot məlumatı</u>"
        else:
            text += "<u>👤İstifadəçi məlumatı</u>"
        text += f'\n\n👨‍💼 Ad : {msg.forward_from["first_name"]}'
        if msg.forward_from["username"]:
            text += f'\n\n🔗 İstifadəçi adı : @{msg.forward_from["username"]} \n\n🆔 ID : <code>{msg.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 ID : `{msg.forward_from["id"]}`'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"❌️Xəta istifadəçi hesabını gizləyib <b><i>{hidden}</i></b>",
                quote=True,
            )
        else:
            text = f"<u>İlətilən (forward) Mesaj məlumatları 👀</u>.\n\n"
            if msg.forward_from_chat["type"] == "channel":
                text += "<u>📢 Kanal</u>"
            if msg.forward_from_chat["type"] == "supergroup":
                text += "<u>🗣️ Grup</u>"
            text += f'\n\n📃 Adı {msg.forward_from_chat["title"]}'
            if msg.forward_from_chat["username"]:
                text += f'\n\n➡️ İstifadəçi adı : @{msg.forward_from_chat["username"]}'
                text += f'\n\n🆔 ID : `{msg.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 ID `{msg.forward_from_chat["id"]}`\n\n'
            await msg.reply(text, quote=True)
