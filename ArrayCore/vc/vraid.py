import os
import re
import asyncio
from pyrogram import Client
from config import bot, call_py, HNDLR, contact_filter, GRPPLAY
from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_streae.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from youtubesearchpython import VideosSearch

from utils import CHAT_TITLE, gen_thumb
from plugins.vc.queues import QUEUE, add_to_queue, get_queue


# video player
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
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()

from .. import (call_py1, call_py2, call_py3, call_py4, call_py5, call_py6, call_py7, call_py8, call_py9, call_py10, call_py11, call_py12, call_py13, call_py14, call_py15, vcbot, HNDLR, SUDO_USERS, Venom1)

aud_list = [
    "./ArrayCore/Audio/VID1.mp4",

@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vraid"], prefixes=HNDLR))
async def vplay(client, e: Message):
 gid = e.chat.id 
 uid = e.from_user.id 
 if gid == uid: 
     inp = e.text[8:]
     chat_ = await Venom1.get_chat(inp) 
     chat_id = chat_.id 
 else: 
     chat_id = gid 
 aud = choice(aud_list)
    if replied:
        if replied.video or replied.document:
            await e.delete()
            huehue = await replied.reply("**🔄 Processing**")
            dl = await replied.download()
            link = replied.link
            if len(e.command) < 2:
                Q = 720
            else:
                pq = e.text.split(None, 1)[1]
                if pq == "720" or "480" or "360":
                    Q = int(pq)
                else:
                    Q = 720
                    await huehue.edit(
                        "`Only 720p, 480p, 360p Allowed` \ n` Now Streaming in 720p`"
                    )

            if replied.video:
                songname = replied.video.file_name[:35] + "..."
            elif replied.document:
                songname = replied.document.file_name[:35] + "..."

            if chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await huehue.delete()
                # await e.reply_to_message.delete()
                await e.reply_photo(
                    photo="https://telegra.ph/file/d6f92c979ad96b2031cba.png",
                    caption=f"""
**#⃣ Video Queued To  {pos}
🏷️ Title: [{songname}]({link})
💬 Chat ID: {chat_id}
🎧 Requested by: {e.from_user.mention}**
""",
                )
            else:
                if Q == 720:
                    hmmm = HighQualityVideo()
                elif Q == 480:
                    hmmm = MediumQualityVideo()
                elif Q == 360:
                    hmmm = LowQualityVideo()
                await call_py.join_group_call(
                    chat_id,
                    AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                    stream_type=StreamType().pulse_stream,
                )
                add_to_queue(chat_id, songname, dl, link, "Video", Q)
                await huehue.delete()
                # await e.reply_to_message.delete()
                await e.reply_photo(
                    photo="https://telegra.ph/file/6213d2673486beca02967.png",
                    caption=f"""
**▶ Start Playing Videos
🏷️ Title: [{songname}]({link})
💬 Chat ID: {chat_id}
🎧 Requested by: {e.from_user.mention}**
""",
                )

    else:
        if len(e.command) < 2:
            await e.reply(
                "**Reply to Audio File or provide something for Searching ...**"
            )
        else:
            await e.delete()
            huehue = await e.reply("**🔎 Searching...")
            query = e.text.split(None, 1)[1]
            search = ytsearch(query)
            Q = 720
            hmmm = HighQualityVideo()
            if search == 0:
                await huehue.edit(
                    "**Didn't Find Anything for the Given Query🤷‍♀️**"
                )
            else:
                songname = search[0]
                title = search[0]
                url = search[1]
                duration = search[2]
                thumbnail = search[3]
                userid = e.from_user.id
                srrf = e.chat.title
                ctitle = await CHAT_TITLE(srrf)
                thumb = await gen_thumb(thumbnail, title, userid, ctitle)
                hm, ytlink = await ytdl(url)
                if hm == 0:
                    await huehue.edit(f"**YTDL ERROR ⚠️** \n\n`{ytlink}`")
                else:
                    if chat_id in QUEUE:
                        pos = add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                        await huehue.delete()
                        # await e.reply_to_message.delete()
                        await e.reply_photo(
                            photo=f"{thumb}",
                            caption=f"""
**#⃣ Video Queued To {pos}
🏷️ Title: [{songname}]({url})
⏱️ Duration: {duration}
💬 Chat ID: {chat_id}
🎧 Requested by: {e.from_user.mention}**
""",
                        )
                    else:
                        try:
                            await call_py.join_group_call(
                                chat_id,
                                AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                                stream_type=StreamType().pulse_stream,
                            )
                            add_to_queue(chat_id, songname, ytlink, url, "Video", Q)
                            await huehue.delete()
                            # await e.reply_to_message.delete()
                            await e.reply_photo(
                                photo=f"{thumb}",
                                caption=f"""
**▶ Start Playing Videos
🏷️ Title: [{songname}]({url})
⏱️ Duration: {duration}
💬 Chat ID: {chat_id}
🎧 Requested by: {e.from_user.mention}**
""",
                            )
                        except Exception as ep:
                            await huehue.edit(f"`{ep}`")

