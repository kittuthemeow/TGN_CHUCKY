# @kittu_the_criminal Dont remove this

from telethon import events, Button, custom
import re, os
from TGNRobot.events import register
from TGNRobot import telethn as tbot
from TGNRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/9f6d14c264fa0ff299206.jpg"
@register(pattern=("/life"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**◐ 𝙽𝚊𝚗 𝚟𝚊𝚗𝚝𝚑𝚞 𝚛𝚘𝚖𝚋𝚊 𝚏𝚊𝚜𝚝 𝚠𝚘𝚛𝚔 𝚊𝚟𝚊𝚗 𝚐𝚊 !** \n\n"
  PIKACHU += "**◐ 𝙽𝚊𝚗 𝚎𝚙𝚘 𝚟𝚞𝚖 𝚖𝚊 𝚠𝚘𝚛𝚔 𝚊𝚟𝚊𝚗 𝚐𝚊**\n\n"
  PIKACHU += "**◐ 𝙽𝚊𝚗: 3.0 Lᴀᴛᴇsᴛ**\n\n"
  PIKACHU += "**◐ 𝙼𝚢 𝚜𝚞𝚙𝚙𝚘𝚛𝚝 :** [𝚜𝚞𝚙𝚙𝚘𝚛𝚝](t.me/chuckmusic)\n\n"
  PIKACHU += "**◐ Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", "https://t.me/chuckmusic"), Button.url("UPDATES", "https://t.me/thanimaibots")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
