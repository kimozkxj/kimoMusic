import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from KimoMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from KimoMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","ڪيمؤ","السورس", "سورس ڪيمؤ"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4a1e93b4660b7de2130c5.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ𝗦𝗢𝗨𝗥𝗦 𝗞𝗜𝗠𝗢 (t.me/vc_di)
么 [ᯓ 𝗗𝗘𝗩 𝗞𝗜𝗠𝗢](t.me/T_lTl_T)
么 [َ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ](t.me/CV_BS)
╰──── • ◈ • ────╯
⍟ 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗦𝗢𝗨𝗥𝗖𝗘 𝗢𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ ᯓ 𝗗𝗘𝗩 𝗞𝗜𝗠𝗢 𝅘𝅥𝅯 . 🕷 › ", url=f"https://t.me/T_lTl_T"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᯓ 𝗖𝗛𝗔𝗡𝗡𝗟𝗘 𖠛›", url=f"https://t.me/vc_di"), 
                    InlineKeyboardButton(
                        "‹ ᯓ 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𖠛›", url=f"https://t.me/CV_BS"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
