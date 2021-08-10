from .config import Config
from logzero import logger
import os
import sys
import time
from pyrogram import Client

from_environment: bool = bool(os.environ.get("env", False))

logger.info(
    """
    ________________________________________
    //          _           _   _         //
    //         | |         | | (_)        //
    //    _ __ | | __ _ ___| |_ _  ___    //
    //   | '_ \| |/ _` / __| __| |/ __|   //
    //   | |_) | | (_| \__ \ |_| | (__    //
    //   | .__/|_|\__,_|___/\__|_|\___|   //
    //   | |            USERBOT           //
    //   |_|                              //
    ----------------------------------------
    """
)
time.sleep(1)

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    logger.error(
        "Python version should be >= 3.6 !\n Stopping userbot..."
    )
    quit(1)

if from_environment:
    logger.info("Selected -> Environment...")

    api_id = os.environ.get("api_id", None)
    api_hash = os.environ.get("api_hash", None)

    USERBOT_VERSION = "v0.0.1"

    COMMAND = os.environ.get("command", "? . _ !".split())
    OWNER_ID = 0
    OWNER_NAME = ""
    OWNER_USERNAME = ""


else:
    logger.info("Selected -> Congifuration file...")

    api_id = Config.api_id
    api_hash = Config.api_hash

    USERBOT_VERSION = Config.USERBOT_VER

    COMMAND = Config.COMMAND

    OWNER_ID = 0
    OWNER_NAME = ""
    OWNER_USERNAME = ""

async def getme():
    global OWNER_ID, OWNER_NAME, OWNER_USERNAME
    me = await app.get_me()
    OWNER_ID = me.id
    OWNER_NAME = me.first_name
    OWNER_USERNAME = me.username

app = Client("my_session", api_id=api_id, api_hash=api_hash)


