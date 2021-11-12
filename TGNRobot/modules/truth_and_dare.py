import html
import random
import TGNRobot.modules.truth_and_dare_string as truth_and_dare_string
from TGNRobot import dispatcher
from telegram import ParseMode, Update, Bot
from TGNRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async
from telegram import ParseMode, Update, ChatPermissions
from telegram.error import BadRequest
import TGNRobot.modules.nekostrings as NEKO
from TGNRobot.modules.helper_funcs.chat_status import (is_user_admin)
from TGNRobot.modules.helper_funcs.extraction import extract_user



@run_async
def nyaa(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        neko_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    nyaa_type = random.choice(("Text", "Gif"))
    if nyaa_type == "Gif":
        try:
            temp = random.choice(nekostrings.NEKO_G)
            reply_to.reply_animation(temp)
        except BadRequest:
            nyaa_type = "Text"

    if nyaa_type == "Text":
        temp = random.choice(nekostrings.NEKO_T)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)




@run_async
def meow(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        meow_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(neko_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    meow_type = random.choice(("Text", "Gif"))
    if meow_type == "Gif":
        try:
            temp = random.choice(nekostrings.CATTO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            nyaa_type = "Text"

    if meow_type == "Text":
        temp = random.choice(nekostrings.CATTO_TEXT)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)

__help__ = """
 • `/nyaa`*:* Use this to get cute Anime Neko Gifs!
 • `/meow`*:* Use this to get cute Real Cat Gifs!

@VALTAOITHEBOT
"""

@run_async
def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

@run_async
def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))
 
@run_async
def abuse(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.ABUSE_STRINGS))

@run_async
def sing(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.SONG_STRINGS))

    
ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SING_HANDLER = DisableAbleCommandHandler("sing", sing)
TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
NYAA = DisableAbleCommandHandler("nyaa", nyaa)
MEOW = DisableAbleCommandHandler("meow", meow)


 
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SING_HANDLER)
dispatcher.add_handler(NYAA)
dispatcher.add_handler(MEOW)
