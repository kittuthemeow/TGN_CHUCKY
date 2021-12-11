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




dispatcher = updater.dispatcher




