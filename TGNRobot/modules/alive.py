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
  PIKACHU = "**β π½ππ ππππππ πππππ ππππ π πππ ππππ ππ !** \n\n"
  PIKACHU += "**β π½ππ πππ πππ ππ π πππ ππππ ππ**\n\n"
  PIKACHU += "**β π½ππ: 3.0 Lα΄α΄α΄sα΄**\n\n"
  PIKACHU += "**β πΌπ’ πππππππ :** [πππππππ](t.me/chuckmusic)\n\n"
  PIKACHU += "**β Tα΄Κα΄α΄Κα΄Ι΄ Vα΄ΚsΙͺα΄Ι΄ : 1.23.0**\n\n"
  BUTTON = [[Button.url("Sα΄α΄α΄α΄Κα΄ CΚα΄α΄", "https://t.me/chuckmusic"), Button.url("UPDATES", "https://t.me/thanimaibots")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
