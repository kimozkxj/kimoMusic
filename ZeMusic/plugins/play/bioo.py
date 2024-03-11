import asyncio
import config
from pyrogram import Client, filters
from ZeMusic import app
from config import OWNER_ID
from ZeMusic.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(filters.command(["زخارف","الزخارف","✨زخارف"], ""))
async def abrag(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("بايوهات عربي", callback_data="bioo1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("بايوهات اجنبي", callback_data="bioo2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اسماء قنوات", callback_data="knwat1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اسماء بنات", callback_data="bnat1 " + str(m.from_user.id))],
        [InlineKeyboardButton("اسماء ولاد", callback_data="asmaa1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("رموز", callback_data="rmows " + str(m.from_user.id))],
        

    ])
    await m.reply_text("• مرحبآ بك عزيزي × قسم ( الزخرفه الجاهزه ) آنقر علي الازرار لآختيار برجك - 💠\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^bioo1 (\\d+)$"))
async def bioo1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """
[" 𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖 〞⦔𓌺 (https://t.me/vc_di)\n- ‏ستنتهي الخيوط التي كُنت أجمع بها نفسي سأصبح مُمَزّقً للأبد .

- قلوبنا مليئة برسائل ، لم تكتب .
‏- لاشيء يمضي، نحن نعتاد فقط
- لا يمُكنك جرحه، هو ممزق بالفعل إلى أجزاء.
- مابال قَلبي لم يَعُد يَشعُر؟
︎
- ‏كُل شيء يحتاج لعناق ليّعود عامراً بعد الخراب .
- ملامحِيِ بدأت تَتحدث عنّ التعب الّذي أحمله بداخليِ.
- حب الخير للغير جهاد ‏لاتقدر عليه كل النفوس..
- الجرح هو المكان الذي يدخلُ منهُ النّور إليك.
- ‏ينتصر صانِعي البَهجة لأنفسهم، لا مُنتظريها.

- إن الحياة بحد ذاتها مملة، حمقاء، قذرة ، تشدك كالمستنقع

‏- سلاماً على من مرّ على مُرِّنا فحلّاه.
- إستمر وكأن لا شيء يؤذيك
- مات شعور الاستغراب اصبح كل شي متوقع
- يُمهل الله أمانينا ولا يهملُها.🕊️ 💞
- لست أحدا وسأظل هكذا إلى الأبد
- لاتعط أحداً قط الفرصة لإضاعة وقتك مرتين 📓🤎
- مازلت اتمنى الشيء الذي يجعلني ابتسم
- مشاعر مُتراكمة..على حافة الإنفِجار 
- كل الذين ربطو سعادتهم بالآخرين ، ماتوا مقتولين من الوحده 

‏- ستموت قبل أن تسمع الكلمات التي تنتظرها

- لا بأس بالوحده ، ان كان الجميع يؤذي قلبك .!.

- لست على ما يرام ولكني أحاول أن ابدو انني بخير.

- جهد كبير في محاربة الأفكار 
- تأقلمت على حزني إلا انه ما زال يبكيني مراراً
"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^bioo2 (\\d+)$"))
async def bioo2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """    
    "[「𝗦𝗢𝗨𝗥𝗦 𝗞𝗜𝗠𝗢」ま ⟧(https://t.me/vc_di)\n
`• 𝑻𝒉𝒆 𝑳𝒐𝒗𝒆𝒓 𝒐𝒇 𝑾𝒉𝒐𝒎 𝑯𝒆 𝑳𝒐𝒗𝒆𝒔 𝒊𝒔 𝑶𝒃𝒆𝒅𝒊𝒆𝒏𝒕 ♡`

`• 𝒆𝒏𝒐𝒖𝒈𝒉 𝒊𝒅𝒆𝒂𝒍, 𝒘𝒓𝒆𝒕𝒄𝒉𝒆𝒅 𝒘𝒐𝒓𝒍𝒅 ၄`

`• 𝑰'𝒎 𝑻𝒉𝒆 𝑶𝒏𝒆 𝑾𝒉𝒐 𝑪𝒓𝒆𝒂𝒕𝒆𝒔 #𝑪𝒉𝒂𝒏𝒄𝒆𝒔 ༒`

`• Smile, no one cares how you feel!`

`• The sweetest thing said in consolation : if I can't light you, I'll turn it off with you.`

➖➖➖➖➖➖➖➖➖➖➖➖➖
    
`• Never let someone who has done nothing tell you how to do anything .`

`• The man who drags you into the shadows, to say "I love you", loves another woman.`

`• It happens a lot to miss, not for anyone but for yourself years ago.`

`• 𝒕𝒉𝒆 𝒅𝒂𝒚 𝒘𝒊𝒍𝒍 𝒄𝒐𝒎𝒆 𝒘𝒉𝒆𝒏 𝒚𝒐𝒖 𝒔𝒕𝒂𝒏𝒅 𝒃𝒆𝒓𝒐𝒓𝒆 𝒚𝒐𝒖𝒓 𝒅𝒓𝒆𝒂𝒎,𝒑𝒓𝒐𝒖𝒅 𝒐𝒓 𝒘𝒉𝒂𝒕 𝒚𝒐𝒖 𝒉𝒂𝒗𝒆 𝒑𝒓𝒐𝒗𝒊𝒅𝒆𝒅,𝒂𝒏𝒅 𝒊𝒓 𝒚𝒐𝒖 𝒂𝒓𝒆 𝒕𝒊𝒓𝒆𝒅 𝒓𝒐𝒓 𝒊𝒕,𝒚𝒐𝒖 𝒘𝒊𝒍𝒍 𝒓𝒊𝒏𝒅 𝒊𝒕 𝒊𝒏 𝒓𝒓𝒐𝒏𝒕 𝒐𝒓 𝒚𝒐𝒖.`

`• Who hates you won't hurt you !Aren't to hurt you only you love.`

➖➖➖➖➖➖➖➖➖➖➖➖➖
 
`• Death ends a life. not a relationship ،`

`• Never let someone who has done nothing tell you how to do anything ،`

`• The only power I owned is that I can stop, suddenly about doing something I love .`

`• No one goes beyond and no one goes beyond everything we tone .`

`• This suffering will deliver a beast, will never give birth .`

➖➖➖➖➖➖➖➖➖➖➖➖➖

`• This suffering will deliver a beast, will never give birth .`

`• Real We are not perfect or extraordinary .`

`• 𝐖𝐇𝐀𝐓 𝐌𝐀𝐊𝐄𝐒 𝐘𝐎𝐔 𝐃𝐈𝐅𝐅𝐄𝐑𝐄𝐍𝐓 ⁞𝐌𝐀𝐊𝐄𝐒 𝐘𝐎𝐔 𝐁𝐄𝐀𝐔𝐓𝐈𝐅𝐔𝐋 ⁽💎🌩₎⇣✿ .`

`• 𝐁𝐄𝐀𝐔𝐓𝐘 𝐈𝐒 𝐖𝐈𝐓𝐇𝐈𝐍 𝐘𝐎𝐔𝐑𝐄 𝐇𝐄𝐀𝐑𝐓 ⚡️🔱 .`

`• 𝐃𝐎𝐍𝐓 𝐆𝐈𝐕𝐄 𝐀𝐍𝐘𝐎𝐍𝐄 𝐎𝐕𝐄𝐑 𝐇𝐈𝐒 𝐕𝐀𝐋𝐔𝐄 😴♩✿⇣.`

➖➖➖➖➖➖➖➖➖➖➖➖➖
    
`• Interest will not come you except from someone who wants you .`

`• 𝙜𝙞𝙫𝙚 𝙡𝙤𝙫𝙚 𝙩𝙤 𝙩𝙝𝙤𝙨𝙚 𝙬𝙝𝙤 𝙜𝙞𝙫𝙚 𝙮𝙤𝙪𝙧 𝙙𝙚𝙩𝙖𝙞𝙡𝙨 𝙩𝙝𝙚𝙞𝙧 𝙨𝙖𝙣𝙘𝙩𝙞𝙩𝙮."`

`• I 𝐛𝐮𝐫𝐧𝐞𝐝 𝐚 𝐥𝐨𝐭 𝐚𝐧𝐝 𝐛𝐞𝐜𝐚𝐦𝐞 𝐚 𝐬𝐭𝐚𝐫 .`

`• 𝒔𝒖𝒅𝒅𝒆𝒏𝒍𝒚 𝒆𝒗𝒆𝒓𝒚𝒕𝒉𝒊𝒏𝒈 𝒇𝒂𝒍𝒍𝒔 𝒂𝒑𝒂𝒓𝒕 𝒂𝒕 𝒐𝒏𝒄𝒆.🤍. ★`

`• 𝒅𝒐𝒏 𝒕 𝒄𝒂𝒓𝒆 𝒂𝒃𝒐𝒖𝒕 𝒘𝒉𝒂𝒕 𝒑𝒆𝒐𝒑𝒍𝒆 𝒘𝒂𝒏𝒕 , 𝒄𝒂𝒓𝒆 𝒂𝒃𝒐𝒖𝒕 ، 𝒘𝒉𝒂𝒕 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 .`

➖➖➖➖➖➖➖➖➖➖➖➖➖
 ⌔︙CH : "@T_lTl_T"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^knwat1 (\\d+)$"))
async def knwat1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """
[●「"𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺」(https://t.me/vc_di)\ 𝗞𝗜𝗠𝗢  🎄꙳.
                𝙆𝙀𝙑𝙄𝙉 𝟐𝟎𝟐𝟏 🎄꙳.
                𝘼𝙉𝙇𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝘾𝙃𝙄𝙏𝙏𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝙎𝘼𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝘾𝙃𝙄𝘾𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝘾𝙃𝙄𝘾𝘼𝙂𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝙀𝘾𝙃𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝙔𝘼𝙔𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝙈𝘼𝙍𝘾𝙀𝙑𝙊 𝟐𝟎𝟐𝟏 🎄꙳.
                𝙔𝙄𝙎𝙆𝘼 𝟐𝟎𝟐𝟏 🎄꙳.
                ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
                𝐌𝐈𝐋𝐀𝐍 🌵
                𝐀𝐍𝐈𝐒𝐀𝐔 🌵
                𝐅𝐑𝐀𝐍𝐂𝐈𝐒𝐎 🌵
                𝐀𝐏𝐑𝐈𝐋  🌵
                ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
                𝙛𝙞𝙘𝙤 🎄
                𝙞𝙨𝙝𝙤 🎄
                𝙖𝙗𝙧𝙖𝙨 🎄
                𝙣𝙞𝙣𝙤 🎄
                ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
                *..⌠𝐒𝐞𝐥𝐯𝐚𝐧𝐚⌡𓊑.
                ..⌠𝐓𝐨𝐛𝐚𝐤⌡𓊑.
                ..⌠𝐄𝐥𝐤𝐚𝐫⌡𓊑.
                ..⌠𝐌𝐚𝐲𝐚⌡𓊑.
                ..⌠𝐓𝐞𝐨𝐨⌡𓊑.
                ..⌠𝐌𝐞𝐚⌡𓊑.
                ..⌠𝐋𝐞𝐥𝐞⌡𓊑.
                ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
                ⌯ ˹𝙆𝙖𝙧𝙖˼ 
                ⌯ ˹𝙉𝙖𝙖𝙧˼ 
                ⌯ ˹𝙂𝙢𝙧˼ 
                ⌯ ˹𝘿𝙚𝙫˼
                ⌯ ˹𝙀𝙫𝙖˼
                ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
                :   ˹𝘾𝘼𝙍𝙊𝙇𝙄𝙉𝙀˼ 𓆪 .
                :   ˹𝘾𝙍𝙔𝙎𝙏𝘼𝙇˼ 𓆪 .
                :   ˹𝙇𝘼𝙐𝙍𝙀𝙉˼ 𓆪 .
                :   ˹𝙆𝘼𝙈𝙄𝙇𝘼˼ 𓆪 .
                :   ˹𝘿𝘼𝙉𝘼˼ 𓆪 .
                :   ˹𝙍𝙄𝙏𝘼˼ 𓆪 .
                : ..................."""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^bnat1 (\\d+)$"))
async def bnat1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """
["●━◉⟞⟦ 𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺」ま ⟧⟝◉━●](https://t.me/vc_di)\n- 𝗞𝗜𝗠𝗢 𐇲.
                - 𝑎𝑛𝑜 𐇲.
                - 𝑡𝑏𝑜 𐇲.
                - 𝑡𝑛𝑜 𐇲.
                - 𝒛𝒉𝒐 𐇲.
                - 𝒛𝒏𝒐 𐇲.
                - 𝒉𝒅𝒐 𐇲.
                - 𝒉𝒃𝒐 𐇲.
                ┉ ┉ ┉ ┉ ┉
                𖥻 𓆩??𝗔𝗭𝗔𝗡𓆪،𖤍
                𖥻 𓆩𝙍𝙚𝙚𝙢𓆪،𖤍
                𖥻 𓆩𝙕𝙖𝙮𝙣𝙖𝙗𓆪،𖤍
                𖥻 𓆩𝙁𝙖𝙩𝙚𝙢𝙖𓆪،𖤍
                𖥻 𓆩𝙍𝙖𝙤𝙖𝙣𓆪،𖤍
                𖥻 𓆩𝙅𝙖𝙣𝙖𝙩𓆪،𖤍
                𖥻 𓆩𝙕𝙖𝙝𝙧𝙖𓆪،𖤍
                𖥻 𓆩𝙉𝙤𝙨𝙖𓆪،𖤍
                ┉ ┉ ┉ ┉ ┉
                - 𝙎 𝘼 𝙉 𝘿 𝙍 𝙄 𝙇 𝘼 : 🇺🇸Ꮠ
                - 𝙍 𝘽 𝘼 𝙉 𝙕 𝙇 : 🇺🇸Ꮠ
                - 𝙎 𝘼 𝙇 𝙇 𝙔 : 🇺🇸Ꮠ
                - 𝙆 𝘼 𝘿 𝙄 𝘼 : 🇺🇸Ꮠ
                - 𝙏 𝙊 𝙏 𝘼 : 🇺🇸Ꮠ
                - 𝘽 𝘼 𝙉 𝙀 𝙉 : 🇺🇸Ꮠ
                ┉ ┉ ┉ ┉ ┉
                𓄼 𝘙 𝘖 𝘡 ༆ 𓄹.
                𓄼 𝘚 𝘖 𝘚 ༆ 𓄹.
                𓄼 𝘛 𝘖 𝘛 ༆ 𓄹.
                𓄼 𝘕 𝘖 𝘕 ༆ 𓄹.
                𓄼 𝘍 𝘖 𝘍 ༆ 𓄹.
                𓄼 𝘑 𝘖 𝘑  ༆ 𓄹.
                𓄼 𝘒 𝘖 𝘒 ༆ 𓄹.
                𓄼 𝘛 𝘕 𝘖 ༆ 𓄹.
                ┉ ┉ ┉ ┉ ┉
                ⌯ ˹𝚁𝙰𝚉𝙰𝙽˼❀ .
                ⌯ ˹ʀɴᴏѕʜ˼❀ .
                ⌯ ˹ᴍᴇᴍᴏ˼❀ .
                ⌯ ˹ʜᴏʀᴇ˼ ❀ .
                ⌯ ˹ѕᴀʀᴀ˼ ❀ .
                ⌯ ˹ѕᴏѕ˼  ❀ .
                ┉ ┉ ┉ ┉ ┉
                𓂐 𝙍𝘼𝙕𝘼𝙉 𖠛.
                𓂐 𝙀𝙇𝙄𝙕𝘼𝘽𝙀𝙏𝙃 𖠛.
                𓂐 𝘼𝙈𝘼𝙉𝘿𝘼 𖠛 .
                𓂐 𝘼𝙉𝘿𝙍𝙀𝘼 𖠛 .
                𓂐 𝙀𝙈𝙀𝙇𝙔 𖠛 .
                𓂐𝙀𝙍𝙄𝙆𝘼 𖠛 .
                𓂐 𝙀𝙑𝘼 𖠛 .
                𓂐 𝘼𝙈𝙔  𖠛 ."""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^asmaa1 (\\d+)$"))
async def asmaa1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """
["●━◉⟞⟦ 「𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺 ⟧⟝◉━●](https://t.me/vc_di)\n  -𓆩𝗞𝗜𝗠𝗢.𖤐𓆪
                -𓆩𝗔𝗠𝗔𝗔𝗥.𖤐𓆪 
                -𓆩𝗠𝗔𝗟𝗘𝗞.𖤐𓆪
                -𓆩𝗔𝗬𝗔𝗗.𖤐𓆪
                -𓆩𝗥𝗔𝗙𝗜𝗗.𖤐𓆪
                -𓆩𝗦𝗕𝗔𝗛.𖤐𓆪
                -𓆩𝗔𝗕𝗔𝗦.𖤐𓆪
                -𓆩𝗛𝗔𝗕𝗜𝗕.𖤐𓆪
                ┉ ┉ ┉ ┉ ┉
                ⌯『𝐀𝐋𝐈』𖤍᭄𓄹
                ⌯『𝐋𝐁𝐍𝐀 』𖤍᭄𓄹
                ⌯『𝐀𝐒𝐄𝐄𝐋』𖤍᭄𓄹
                ⌯『𝐒𝐇𝐄𝐑𝐄𝐍』𖤍᭄𓄹
                ⌯『𝐌𝐔𝐒𝐓𝐀𝐅𝐀』𖤍᭄𓄹
                ┉ ┉ ┉ ┉ ┉
                𓆩𝒌𝒉𝒂𝒍𝒆𝒅𓆪 🖤.
                𓆩𝑶𝒎𝒂𝒓𓆪 🖤.
                𓆩𝑯𝒂𝒛𝒂𝒎𓆪 🖤.
                𓆩𝑯𝒂𝒕𝒂𝒎𓆪 🖤.
                𓆩𝑶𝒔𝒂𝒎𝒂𓆪 🖤.
                𓆩𝑯𝒂𝒅𝒐𓆪 🖤.
                𓆩𝑯𝒂𝒊𝒅𝒂𝒓𓆪 🖤.
                𓆩𝑮𝒉𝒂𝒍𝒆𝒃𓆪 🖤.
                𓆩𝑨𝒌𝒓𝒂𝒎𓆪 🖤.
                𓆩𝑯𝒂𝒔𝒐𝒏𝒆𓆪 🖤.
                𓆩𝑯𝒂𝒎𝒐𝒅𝒊𓆪 🖤.
                𓆩𝒗𝒊𝒓𝒐𝒔𓆪 🖤.
                𓆩𝑶𝒓𝒂𝒔𓆪 🖤.
                𓆩𝑺𝒂𝒍𝒊𝒉𓆪 🖤.
                ┉ ┉ ┉ ┉ ┉
                「𝘔𝘦𝘳𝘰 𐃣.
                「𝘋𝘢𝘦𝘷 𐃣.
                「𝘌𝘷𝘢 𐃣.
                「𝘋𝘮𝘢𝘳 𐃣.
                「𝘑𝘮𝘳𝘢 𐃣.
                𓆩𝑨𝒃𝒐𝒅𝒆𓆪 🖤.
                𓆩𝑴𝒖𝒔𝒕𝒂𝒇𝒂𓆪 🖤.
                𓆩𝑴𝒂𝒉𝒅𝒊𓆪 🖤.
                𓆩𝑸𝒂𝒔𝒂𝒎𓆪 🖤.
                𓆩𝑹𝒂𝒔𝒉𝒂𝒅𓆪 🖤.
                𓆩𝑨𝒅𝒏𝒂𝒏𓆪 🖤.
                𓆩𝑺𝒂𝒓𝒎𝒂𝒅𓆪 🖤.
                𓆩𝑯𝒂𝒔𝒂𝒏𓆪 🖤.
                𓆩𝑵𝒂𝒛𝒂𝒓𓆪 🖤.
                𓆩𝑴𝒐𝒉𝒂𝒎𝒆𝒅𓆪 🖤.
                𓆩𝑲𝒂𝒓𝒂𝒓𓆪 🖤.
                𓆩𝑨𝒉𝒎𝒆𝒅𓆪 🖤.
                𓆩𝑨𝒅𝒂𝒎𓆪 🖤.
                𓆩𝑯𝒖𝒔𝒔𝒊𝒆𝒏𓆪 🖤.
                𓆩𝑨𝒍𝒐𝒔𝒉𓆪 🖤.
                𓆩𝑹𝒂𝒔𝒐𝒖𝒍𓆪 🖤.
                ┉ ┉ ┉ ┉ ┉
                𓆩𝚁𝙾𝙽𝙴𓆪  🇺🇸.
                𓆩𝙴𝚅𝙰𝙽𓆪  🇺🇸.
                𓆩𝙹𝙰𝙺𓆪  🇺🇸.
                𓆩𝚃𝙾𝙼𓆪  🇺🇸.
                𓆩𝙹𝙾𝙽𓆪  🇺🇸.
                𓆩𝙰𝙷𝙼𝙸𝙳𓆪🎗️ ꙰
                𓆩𝙰𝙻𝙾𝚂𝙷𓆪🎗️ ꙰
                𓆩𝚂𝙰𝙹𝙰𝙳𓆪🎗️ ꙰
                𓆩𝚂𝙱𝙰𝙰𝙷𓆪🎗️ ꙰
                𓆩𝙷𝙰𝙸𝚃𝙷𝙼𓆪🎗️ ꙰
                𓆩𝙷𝚄𝚂𝚂𝙴𝙸𝙽𓆪🎗️ ꙰
                𓆩𝙼𝚄𝙷𝙰𝙼𝙼𝙰𝙳𓆪🎗️ ꙰
                ┉ ┉ ┉ ┉ ┉
                - 𝙎 𝘼 𝙄 𝙆 𝙊 : 🇺🇸Ꮠ
                - 𝙈 𝘼 𝙍 𝘾 𝙊 : 🇺🇸Ꮠ
                - 𝙎 𝘼 𝙉 𝙔 : 🇺🇸Ꮠ
                - 𝗥 𝗥 9 𝗥 7 : 🇺🇸Ꮠ
                - 𝙏 𝙃 𝘼 𝙈 𝙀 𝙍 : 🇺🇸Ꮠ
                - 𝘽 𝘼 𝙉 : 🇺🇸Ꮠ
                ┉ ┉ ┉ ┉ ┉
                𓂐 𝘼𝙈𝙀𝙍 𖠛 .
                𓂐 𝙆𝘼𝙈𝙀𝙇 𖠛.
                𓂐 𝙃𝙈𝙊 𖠛 .
                𓂐 𝙅𝙊𝙅 𖠛 ."""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)
    
    
@app.on_callback_query(filters.regex("^rmows (\\d+)$"))
async def rmows(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    abrag_text = """
["●━◉⟞⟦ 𓌹⦓〝𝗞𝗜𝗠𝗢 𝗠𝗨𝗦𝗜𝗖〞⦔𓌺 ⟧⟝◉━●](https://t.me/vc_di)\n•𓃠 .𓅿 . 𓃠 . 𓃒 . 𓅰 . 𓃱∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿   ⎔ ⎕ ⎖ ⎗ ⎘ ⎙ ⎚ ⎛ ⎜ ⎝ ⎞  ⏞ ⏟ ⏠ ⏡ ⏢ ⏣ ⏤ ⏥ ⏦ ␋ ␢ ▫️ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▷ ▸ ▹ ► ▻ ▼ ▽ ▾ ▿  ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐ ◑ ◒ ◓ ◔ ◔ʊ ◕  ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◸ ◹ ◺  ☓☠️ ☡☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟ ♠️ ♡ ♢  ♩ ♪ ♫ ♬ ♭ ♮ ♯ ♰ ♱ ♻️ ♼ ♽ ⚆ ⚇ ⚈ ⚉ ⚊ ⚋ ⚌ ⚍ ⚎ ⚏ ⚐ ⚑ ✐ ✑ ✒️ ✓ ✔️ ✕ ✖️ ✗ ✘ ✙ ✚ ✛ ✜  ✞ ✟ ✠ ✢ ✣ ✤ ✥ ✦ ✧ ✧♱ ✩ ✪ ✫ ✬ ✭ ✮ ✯ ✰ ✱ ✲  ✵ ✶ ✷ ✸ ✹ ✺  ❍ ❏ ❐ ❑ ❒ ❖  ❘ ❙ ❚ ❛ ❜ ❝ ❞ ❡ ❢  ❥ ❦ ❧ ❨ ❩ ❪ ❫ ❬ ❭ ❮ ❯ ❰ ❱ ❲ ❳ ❴ ❵ ➔ ➘  ➾ ⟀ ⟁ ⟂ ⟃ ⟄ ⟇ ⟈ ⟉ ⟊ ⟐ ⟑ ⟒ ⟓ ⟔ ⟕ ⟖ ⟗ ⟘ ⟙ ⟚ ⟛ ⟜ ⟝ ⟞ ⟟ ⟠ ⟡ ⟢ ⟣ ⟤ ⟥ ⟦ ⟧ ⟨ ⟩ ⟪ ⟫ ⟰ ⟱ ⟲ ⟳ ⟴ ⟵ ⟶ ⟷ ⟸ ⟹ ⟺ ⟻ ⟼ ⟽ ⟾ ⟿ ⤀ ⤦ ⤧ ⤨ ⤩ ⤪ ⤫ ⤬ ⤭ ⤮ ⤯ ⤰ ⤱ ⤲ ⤳ ⤶ ⤷ ⤸ ⤹ ⤺ ⤻ ⤼ ⤽ ⤾ ⤿ ⥀ ⥁ ⥂ ⥃ ⥄ ⥅ ⥆ ⥇ ⥈ ⥉ ⥊ ⥋ ⥌ ⥍ ⥎ ⥏ ⥐ ⥑ ⥒ ⥓ ⥔ ⥕ ⥖ ⥗ ⥘ ⥙ ⥚ ⥛ ⥜ ⥝ ⥞ ⥟ ⥠ ⥡ ⥢ ⥣ ⥤ ⥥ ⥦ ⥧ ⥨ ⥩ ⥪ ⥫ ⥬ ⥭ ⥮ ⥯ ⥰ ⥱ ⥲ ⥳ ⥴ ⥵ ⥶ ⥷ ⥸ ⥹ ⥺ ⥻ ⥼ ⥽ ⥾ ⥿ ⦀ ⦁ ⦂ ⦃ ⦄ ⦅ ⦆ ⦇ ⦈ ⦉ ⦊ ⦋ ⦌ ⦍ ⦎ ⦏ ⦐ ⦑ ⦒ ⦓ ⦔ ⦕ ⦖ ⦗ ⦘ ⦙ ⦚ ⦛ ⦜ ⦝ ⦞ ⦟ ⦠ ⦡ ⦢ ⦣ ⦤ ⦥ ⦦ ⦧ ⦨ ⦩ ⦪ ⦫ ⦬ ⦭ ⦮ ⦯ ⦰ ⦱ ⦲ ⦳ ⦴ ⦵ ⦶ ⦷ ⦸ ⦹ ⦺ ⦻ ⦼ ⦽ ⦾ ⦿ ⧀ ⧁ ⧂ ⧃ ⧄ ⧅ ⧆ ⧇ ⧈ ⧉ ⧊ ⧋ ⧌ ⧍ ⧎ ⧏ ⧐ ⧑ ⧒ ⧓ ⧔ ⧕ ⧖ ⧗ ⧘ ⧙ ⧚ ⧛ ⧜ ⧝ ⧞ ⧟ ⧡ ⧢ ⧣ ⧤ ⧥ ⧦ ⧧ ⧨ ⧩ ⧪ ⧫ ⧬ ⧭ ⧮ ⧯ ⧰ ⧱ ⧲ ⧳ ⧴ ⧵ ⧶ ⧷ ⧸ ⧹ ⧺ɷ
 ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎
₁ ₂ ₃ ₄ ₅ ₆ ₇ ₈ ₉ ₀
 ﹎﹎﹎﹎﹎﹎﹎﹎﹎﹎"""
    await m.message.reply_text(abrag_text, reply_to_message_id=mid)
    