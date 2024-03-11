import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["ڪيمؤ","المبرمج ڪيمؤ","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4a1e93b4660b7de2130c5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𓆩𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺](https://t.me/T_lTl_T)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @T_lTl_T ❫
◉ 𝙸𝙳      : ❪ `6570384352` ❫
◉ 𝙱𝙸𝙾    : ❪ for me ( @vc_di )  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْ𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺", url=f"https://t.me/T_lTl_T"), 
                 ],[
                   InlineKeyboardButton(
                        "𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺", url=f"https://t.me/T_lTl_T"),
                ],

            ]

        ),

    )
