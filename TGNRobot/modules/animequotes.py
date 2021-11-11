# @VALTAOITHEBOT Dont remove this

import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import TGNRobot.modules.animequotes_strings as animequotes_strings
from TGNRobot import dispatcher
from TGNRobot.modules.disable import DisableAbleCommandHandler
from TGNRobot.modules.helper_funcs.chat_status import (is_user_admin)
from TGNRobot.modules.helper_funcs.extraction import extract_user

@run_async
def animequotes(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(animequotes_strings.QUOTES_IMG))

__help__ = """
 • `/Beybladequotes`*:* gives random Beyblade memes
 @VALTAOITHEBOT
"""
ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("Beybladequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)

__mod_name__ = "Beybladequotes"
__command_list__ = [
    "Beybladequotes"
]
__handlers__ = [
    ANIMEQUOTES_HANDLER
]
