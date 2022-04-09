import asyncio
import datetime
import logging
import os
import re
import sys

from asyncio import sleep
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputVideoStream, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio, HighQualityVideo,
                                                  LowQualityVideo, MediumQualityVideo)

from ArrayCore.vc.queues import QUEUE, add_to_queue, get_queue, clear_queue
from pytgcalls.types.input_stream import VideoParameters

from .. import (call_py1, call_py2, call_py3, call_py4,
                    call_py5, call_py6, call_py7, call_py8,
                    call_py9, call_py10, call_py11, call_py12,
                    call_py13, call_py14, call_py15, vcbot, 
                    HNDLR, SUDO_USERS, Venom1)

logging.basicConfig(level=logging.INFO)

aud_list = [
    "./ArrayCore/Audio/VID1.mp4",
]


@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["vd"], prefixes=HNDLR))
async def vcraid(_, e: Message):
    gid = e.chat.id
    uid = e.from_user.id
    if gid == uid:
        inp = e.text[8:]
        chat_ = await Venom1.get_chat(inp)
        chat_id = chat_.id
    else:
         chat_id = gid
    aud = choice(aud_list)
    if:
        TheVenomXD = await e.reply_text("**Starting VC raid**")
        link = f"https://itshellboy.tk/{aud[1:]}"
        dl = aud
        songname = aud[18:]
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await TheVenomXD.delete()
            await e.reply_text(f"**> Raiding in:** {chat_.title} \n\n**> Audio:** {songname} \n**> Position:** #{pos}")
        else:
            if call_py1:
                await call_py1.join_group_call(
                    chat_id,
                    InputAudioStream(
                        aud_list,
                        AudioParameters(
                            bitrate=48000,
                        ),
                    ),
                    InputVideoStream(
                        video_file,
                        VideoParameters(
                            width=1280,
                            height=720,
                            frame_rate=20,
                        ),
                    ),
                    stream_type=StreamType().pulse_stream,
                )
                await msg.edit("**Started Video Stream!**")
                await idle()
