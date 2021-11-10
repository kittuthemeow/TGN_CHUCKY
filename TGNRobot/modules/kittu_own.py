import html
import random
import TGNRobot.modules.kittu_own as kittu_ownstring
from TGNRobot import dispatcher
from telegram import ParseMode, Update, Bot
from TGNRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def abuse(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(kittu_ownstring.abuse))

@run_async
def sing(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(kittu_ownstring.sing))

    
ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)
SING_HANDLER = DisableAbleCommandHandler("sing", sing)

dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SING_HANDLER)
