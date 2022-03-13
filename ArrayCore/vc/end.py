import os

from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import clear_queue, QUEUE
from .. import call_py1, vcbot, HNDLR, SUDO_USERS



@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["end"], prefixes=HNDLR))
async def ping(_, e: Message):
    chat_id = e.chat.id
    if chat_id in QUEUE:
        try:
            await call_py1.leave_group_call(chat_id)
            clear_queue(chat_id)
            await e.reply_text("**End**")
        except Exception as ex:
            await e.reply_text(f"**ERROR** \n`{ex}`")
    else:
        await e.reply_text("**Nothing is playing !**")
