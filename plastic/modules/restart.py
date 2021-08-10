from plastic.__main__ import restart_all
from plastic import app, COMMAND, logger
from pyrogram import filters
from pyrogram.types import Message

@app.on_message(filters.user("self") & filters.command("restart", COMMAND))
async def res_bot(client, message: Message):
    logger.info("Restarting Modules ...")
    await message.edit("Restarted Successfully.")
    await restart_all()