from plastic import logger
from speedtest import Speedtest
from pyrogram import filters, Client
from pyrogram.types import Message
from plastic import app, COMMAND
from plastic.helpers.formatter import speedtest_convert
import time

__MODULE__ = "speed_test"

#__HELP__ = """
#Check your Internet Speed.
#"""

ST_RESULT = """
--**Speedtest Result :**--
Download : `{}`
Upload : `{}`
Ping : `{}`
ISP : `{}`
Server : `{}, {}`
"""

@app.on_message(filters.user("self") & filters.command("speedtest", COMMAND))
async def spd_test(client: Client, message: Message):
    logger.info("Performing Speedtest ...")
    await message.edit("Testing Speed...")
    test = Speedtest()
    test.get_best_server()
    test.upload()
    test.download()
    result = test.results.dict()

    await message.edit(
        ST_RESULT.format(
        speedtest_convert(result['download']),
        speedtest_convert(result['upload']),
        result['ping'],
        result['client']['isp'],
        result['server']['sponsor'], result['server']['country']
    )
    )
