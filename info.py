import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '29728878'))
API_HASH = environ.get('API_HASH', 'a961168f7807061e77e1fb39c3f6ef71')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5294914915 7033385522').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/B4UOwnerBot')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002179479692'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002150820537 -1002235533210').split()]
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_URI2 = environ.get('DATABASE_URI2', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Yaduvanshi')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002470952565'))
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/T-5.jpg')

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002480353700'))
URL = environ.get('URL', 'specified-ricky-pwvidyapeeth-fe32bd8d.koyeb.app')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002471108414'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/How_to_open_movielink")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/How_to_open_movielink")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/How_to_open_movielink")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "597e5e39d64825dedf5b43361e9a57e5d1ab6be5")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shortxlinks.com")
SHORTENER_API2 = environ.get("SHORTENER_API2", "e36fc95289f44c5b5af8ef6daa44dcf75ddaecd1")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "Tryshort.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "1dacaa27ce824e44b95f1b6a11939575205d1fa9")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "Instantearn.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "28800"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002041612661'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1800))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
