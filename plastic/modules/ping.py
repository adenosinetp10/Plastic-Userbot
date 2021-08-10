import time
from pyrogram import filters
from plastic import COMMAND, app


@app.on_message(filters.user("self") & filters.command(["ping"], COMMAND))
async def ping(client, message):
	start_time = time.time()
	await message.edit("Pong!")
	end_time = time.time()
	ping_time = float(end_time - start_time)
	await message.edit(f"**Ping :** `{round(ping_time*100)}ms`")
