import asyncio
import time
import importlib

from plastic import app, COMMAND, logger, getme, OWNER_ID, OWNER_NAME, OWNER_USERNAME
from pyrogram import idle
from plastic.modules import MODULES

loop = asyncio.get_event_loop()


async def reload_userbot():
    await app.start()
    for module in MODULES:
        imported_module = importlib.import_module("plastic.modules." + module)
        importlib.reload(imported_module)


async def restart_userbot():
    importlib.reload(importlib.import_module("plastic.modules"))
    from plastic.modules import MODULES
    await app.restart()
    await getme()
    for module in MODULES:
        imported_module = importlib.import_module("plastic.modules." + module)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
        importlib.reload(imported_module)


async def restart_all():
    asyncio.get_event_loop().create_task(restart_userbot())


async def start_userbot():
    await app.start()
    await getme()
    await app.stop()
    logger.info("starting Userbot ...")
    await app.start()
    for modul in MODULES:
        imported_module = importlib.import_module("plastic.modules." + modul)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
    
    logger.info("----IDLE----")
    await idle()




if __name__ == "__main__":
    USERBOT_RUNTIME = int(time.time())
    loop.run_until_complete(start_userbot())