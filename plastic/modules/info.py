from plastic import app, COMMAND, USERBOT_VERSION
from pyrogram import filters
from pyrogram.types import Message


INFO = """
**ID : ** `{}`
**First Name : ** `{}`
**Last Name : ** `{}`
**User Name : ** `{}`
**DC ID : ** `{}`
**Link :** [here]({}) 
"""

@app.on_message(filters.user("self") & filters.command(["me"], COMMAND))
async def get_myself_client(client, message: Message):
	me = await app.get_me()
	await message.edit(
        INFO.format(
            me.id,
            me.first_name,
            me.last_name,
            me.username,
            me.dc_id,
            f"tg://user?id={me.id}"
        )
    )
	