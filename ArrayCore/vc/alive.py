from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import (Venom1, Venom2, Venom3, Venom4,
                Venom5, Venom6, Venom7, Venom8,
                Venom9, Venom10, Venom11, Venom12,
                Venom13, Venom14, Venom15, HNDLR,
                SUDO_USERS, vcbot, ALIVE_PIC, __version__)                   

Array = ALIVE_PIC or "https://telegra.ph/file/fea7a0ef15a02dd5e4aac.jpg"

 
@vcbot.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
async def _Alive(_, e: Message):
    ids = 0
    try:
        if Venom1:
            ids += 1
        if Venom2:
            ids += 1
        if Venom3:
            ids += 1
        if Venom4:
            ids += 1
        if Venom5:
            ids += 1
        if Venom6:
            ids += 1
        if Venom7:
            ids += 1
        if Venom8:
            ids += 1
        if Venom9:
            ids += 1
        if Venom10:
            ids += 1
        if Venom11:
            ids += 1
        if Venom12:
            ids += 1
        if Venom13:
            ids += 1
        if Venom14:
            ids += 1
        if Venom15:
            ids += 1
        Array_msg = f"𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 𝗛𝗲𝗿𝗲. 🔥 \n\n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Array_msg += f"► Aʀʀᴀʏ ᴠᴇʀsɪᴏɴ : `{__version__}` \n"
        Array_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Array_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Array_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/DNHxHELL) \n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• Channel •", url="https://t.me/ArrayCore")
                ], [
                    InlineKeyboardButton(
                        "• Repo •", url="https://github.com/desinobita/TgVcUsers")
                ]],
        ),
    ) 
    except Exception as lol:         
        Array_msg = f"𝗔𝗿𝗿𝗮𝘆𝗖𝗼𝗿𝗲 𝗛𝗲𝗿𝗲. 🔥 \n\n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Array_msg += f"► Aʀʀᴀʏ ᴠᴇʀsɪᴏɴ : `{__version__}` \n"
        Array_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Array_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](https://t.me/DNHxHELL) \n"
        Array_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=Array,
        caption=Array_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• Channel •", url="https://t.me/ArrayCore"),
                ],
                [
                    InlineKeyboardButton("• Repo •", url="https://github.com/desinobita/TgVcUsers"),
                ],
            ],
        ),
    ) 
