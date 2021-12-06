import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/e9d3e8f2a440894c55fc3.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [🕊️⃝‌⭕🇰𝖎𝖙𝖙𝖚🇹𝖙𝖍𝖊 🇲𝖊⭕](https://t.me/Kittu_the_criminal) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @chuckmusic «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡ᴏᴡɴᴇʀ🔥", url=f"https://t.me/Kittu_the_criminal"),
        InlineKeyboardButton(" sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ  💫", url=f"https://t.me/chuckmusic"),
      ],[
        InlineKeyboardButton("ɢʙᴀɴ ʟᴏɢs ❣️", url="https://t.me/chuckmusicupdate"),
        InlineKeyboardButton("ᴋᴀʀᴍᴀ sᴄᴀɴɴᴇʀ ⚡", url="https://t.me/karma_appeal"),
      ],[
        InlineKeyboardButton("⚡ sᴄᴀɴɴᴇʀ ", url="https://t.me/Karma_scanner"),
        InlineKeyboardButton("ᴏᴜʀ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴛᴇᴀᴍ ➡️", url="https://t.me/chuckmusicupdate/536"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
