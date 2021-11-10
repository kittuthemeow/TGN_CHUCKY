import html
import random
import TGNRobot.modules.truth_and_dare_string as truth_and_dare_string
from TGNRobot import dispatcher
from telegram import ParseMode, Update, Bot
from TGNRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

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

 
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(SING_HANDLER)
