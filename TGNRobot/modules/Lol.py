
#this module only Created in @VegetaRobot

from TGNRobot.events import register
from TGNRobot import telethn as tbot
import os
from TGNRobot import DEV_USERS
import random
from PIL import Image, ImageDraw, ImageFont


logopics = [
 
 "./TGNRobot/N2/meme/-6080291618361028275_120.jpg"
 
]
 

logofonts = [
 
 "./TGNRobot/N2/meme/memefont1.otf"
 
]
 
 

 


pic_choice = random.choice(logopics)
font_choice = random.choice(logofonts)


@register(pattern="^/2meme ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == DEV_USERS:
     pass
 else:

    if not quew:
       await event.reply('**Provide Some Text To Draw!**')
       return
    else:
       pass
 await event.reply('**Your meme making...wait!**')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(pic_choice)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 540
    fillcolor = "red"
    shadowcolor = "blue"
    font = ImageFont.truetype(font_choice , 40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.20)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(245, 245, 245))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=13, stroke_fill="blue")
    fname2 = "Vegeta.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="**REDAY**")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'**Error **, {e}')

   
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


mod_name = "memeCreat"

