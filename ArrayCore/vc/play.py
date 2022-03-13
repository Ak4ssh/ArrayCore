import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)
from youtubesearchpython import VideosSearch

from ArrayCore.vc.queues import QUEUE, add_to_queue, get_queue
from . import CHAT_TITLE, gen_thumb
from .. import vcbot, call_py1, HNDLR, SUDO_USERS

logging.basicConfig(level=logging.INFO)

print("Starting.....")


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        # CHANGE THIS BASED ON WHAT YOU WANT
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@vcbot.on_message(filters.user(SUDO_USERS) & ~filters.private & filters.command(["play"], prefixes=HNDLR))
async def ping(_, e: Message):
    replied = e.reply_to_message
    chat_id = e.chat.id
    if replied:
        if replied.audio or replied.voice:
            await e.delete()
            TheVenomXD = await replied.reply_text("**Transcoding Mp3...**")
            dl = await replied.download()
            link = replied.link
            if replied.audio:
                if replied.audio.title:
                    songname = replied.audio.title[:35] + "..."
                else:
                    songname = replied.audio.file_name[:35] + "..."
            elif replied.voice:
                songname = "Voice Note"
            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await TheVenomXD.delete()
                await e.reply_text(f"**> Playing in:** {e.chat.title} \n\n**> Song:** {songname} \n**> Position:** #{pos}")
            else:
                await call_py1.join_group_call(chat_id, AudioPiped(dl), stream_type=StreamType().pulse_stream)
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                await TheVenomXD.delete()
                await e.reply_text(f"**> Playing in:** {e.chat.title} \n\n**> Song:** {songname} \n**> Position:** Currently Playing")
    else:
        if len(e.command) < 2:
            await e.reply_text("Reply to Audio File or provide something for Searching ...")
        else:
            await e.delete()
            TheVenomXD = await e.reply_text("__Searching...__")
            query = e.text.split(" ", 1)[1]
            search = ytsearch(query)
            if search == 0:
                await TheVenomXD.edit("`Didn't Find Anything for the Given Query`")
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = e.from_user.id
                user_name = e.from_user.first_name
                srrf = e.chat.title
                ctitle = await CHAT_TITLE(srrf)
                thumb = await gen_thumb(thumbnail, title, userid, ctitle)
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await TheVenomXD.edit(f"**YTDL ERROR ️!** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                        await TheVenomXD.delete()
                        await e.reply_photo(photo=thumb, caption=f"**> Playing in:** {srrf} \n\n**> Song:** {songname} \n**> Position:** #{pos} \n\n**BY:** [{user_name}]({userid})")
                    else:
                        try:
                            await call_py1.join_group_call(chat_id, AudioPiped(ytlink), stream_type=StreamType().pulse_stream)
                            add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                            await TheVenomXD.delete()
                            await e.reply_photo(photo=thumb, caption=f"**> Playing in:** {srrf} \n\n**> Song:** {songname} \n**> Position:** Currently Playing \n\n**By:** [{user_name}]({userid})")
                        except Exception as ep:
                            await TheVenomXD.edit(f"`{ep}`")

