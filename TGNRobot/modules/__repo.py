import os
from pyrogram import Client, filters
from pyrogram.types import *

from TGNRobot.conf import get_str_key
from TGNRobot import pbot

REPO_TEXT = "**A Powerful [BOT](https://telegra.ph/file/cab6825dea9263d347831.jpg) to Make Your Groups Secured and Organized ! \n\n↼ Øwñêr ⇀ : 『 [Akki](t.me/godfatherakki) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @CHUCKYMUSIC_BOT «««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("⚡Owner 🔥", url="t.me/Kittu_the_criminal"),
        InlineKeyboardButton(" ᴊᴏɪɴ 💫", url="https://t.me/Superior_Bots"),
      ],[
        InlineKeyboardButton("ᴛɢɴ ᴏᴡɴᴇʀ ❣️", url="https://t.me/chuckmusic"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/chuckmusic"),
      ],[
        InlineKeyboardButton("⚡ ᴜᴘᴅᴀᴛᴇꜱ ☑️", url="https://t.me/chuckmusicupdate"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ➡️", url="https://t.me/Kittu_the_criminal"),
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
