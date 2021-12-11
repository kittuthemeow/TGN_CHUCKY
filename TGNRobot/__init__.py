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






updater = Telegramcilent.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = Telegramclient("layla", API_ID, API_HASH)
pbot = Client("robot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher




