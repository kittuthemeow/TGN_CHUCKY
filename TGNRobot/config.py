import json
import os

def get_user_list(config, key):
    with open("{}/TGNRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

LOGGER = "True"
ALLOW_EXCL = ""
BL_CHATS = ""
BAN_STICKER = ""
BOT_ID = "2003043761"
BOT_USERNAME = "@Chuckymusic_bot"
CASH_API_KEY = ""
DATABASE_URL = ""
DEL_CMDS = "true"
DEMONS  = "2057139792 1993128405 1181494383 1393492535 1904184235 1234465167 1480007084 1912630709"
DEV_USERS = "2057139792 1993128405 1181494383 1393492535 1904184235 1234465167 1480007084 1912630709"
ENV = ""
DRAGONS = "2057139792 1993128405 1181494383 1393492535 1904184235 1234465167 1480007084 1912630709"
EVENT_LOGS = "-1001570400013"
INFOPIC = "true"
JOIN_LOGGER = "-1001570400013"
MONGO_DB_URI = "mongodb+srv://Izazkhan:izazkhan@cluster0.hlltt.mongodb.net/project0?retryWrites=true&w=majority"
No_LOAD = "true"
OWNER_ID = "2068952393"
OWNER_USERNAME = "@Kittu_the_criminal"
PORT= ""
REM_BG_API_KEY= "dxsh728mZMDmj4ijSZCNPZig"
SQLALCHEMY_DATABASE_URI = "sqldbtype://username:pw@hostname:port/db_name"
STRICT_GBAN = "true"
STRICT_GMUTE = "true"

SUPPORT_CHAT = "chucky_support"

TIGERS ="2057139792 1993128405 1181494383 1480007084 1912630709 2117266789 1044655712"

TOKEN = "2003043761:AAHCRFosoRfjJMrcsJpDrGwnOTQddWG3Ul8"

class Production(config):
    LOGGER = True


class Development(config):
    LOGGER = True
