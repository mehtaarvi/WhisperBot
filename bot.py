from telethon import events, TelegramClient, Button
import logging
from telethon.tl.functions.users import GetFullUserRequest as us
import os


logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None)

bot = TelegramClient(
        "Whisper",
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        ).start(
                bot_token=TOKEN
                )
db = {}

@bot.on(events.NewMessage(pattern="^[!?/]start$"))
async def stsrt(event):
    await event.reply(
            "**𝐇𝐄𝐘 [{}](tg://user?id={})\n 𝐈 𝐀𝐌 𝐀 𝐖𝐇𝐈𝐒𝐏𝐄𝐑 𝐁𝐎𝐓.\n 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 [𝐄𝐕𝐄𝐑𝐄𝐓𝐓](https://t.me/YOUR_DEVIL_DAD)\n\n ..........𝐓𝐇𝐀𝐍𝐊𝐘𝐎𝐔.........!**",
            buttons=[
                [Button.switch_inline("Go Inline", query="")]
                ]
            )


@bot.on(events.InlineQuery())
async def die(event):
    if len(event.text) != 0:
        return
    me = (await bot.get_me()).username
    dn = event.builder.article(
            title="It's a whisper bot deployed by [𝐄𝐕𝐄𝐑𝐄𝐓𝐓](https://t.me/YOUR_DEVIL_DAD)!",
            description="It's a whisper Bot!\n(c) Reeshuxd",
            text=f"**It's a whisper bot**\n`@{me} wspr UserID|Message`\n**[𝐄𝐕𝐄𝐑𝐄𝐓𝐓](https://t.me/YOUR_DEVIL_DAD)**",
            buttons=[
                [Button.switch_inline(" Go Inline ", query="wspr ")]
                ]
            )
    await event.answer([dn])
    
@bot.on(events.InlineQuery(pattern="wspr"))
async def inline(event):
    me = (await bot.get_me()).username
    try:
        inp = event.text.split(None, 1)[1]
        user, msg = inp.split("|")
    except IndexError:
        await event.answer(
                [], 
                switch_pm=f"@{me} [UserID]|[Message]",
                switch_pm_param="start"
                )
    except ValueError:
        await event.answer(
                [],
                switch_pm=f"Give a message too!",
                switch_pm_param="start"
                )
    try:
        ui = await bot(us(user))
    except BaseException:
        await event.answer(
                [],
                switch_pm="Invalid User ID/Username",
                switch_pm_param="start"
                )
        return
    db.update({"user_id": ui.user.id, "msg": msg, "self": event.sender.id})
    text = f"""
Ye Mssg bhej diya mene shhshhhah🤫🤫🤫🤫
To [{ui.user.first_name}](tg://user?id={ui.user.id})!
Click The Below Button To See The Message!
**Note:** __Only {ui.user.first_name} can open this!__
    """
    dn = event.builder.article(
            title="Its a secret message! M Kisi ko nahi btaunga 👁",
            description="It's a secret message! Sssh!",
            text=text,
            buttons=[
                [Button.inline(" Show Message! ", data="wspr")]
                ]
            )
    await event.answer(
            [dn],
            switch_pm="It's a secret message! M kisi ko nhi btaunga 👁",
            switch_pm_param="start"
            )


@bot.on(events.CallbackQuery(data="wspr"))
async def ws(event):
    user = int(db["user_id"])
    lol = [int(db["self"])]
    lol.append(user)
    if event.sender.id not in lol:
        await event.answer("🔐 This message is NOT for you (𝙠𝙮𝙪  𝙟𝙖𝙡𝙖𝙣 𝙝𝙤 𝙧𝙝𝙞 𝙝 𝙠𝙮𝙖𝙖 𝙩𝙪𝙢𝙠𝙤 😂😂𝑻𝑯𝑶𝑫𝑨  𝑶𝑹 𝑱𝑳𝑶 𝑱𝑳𝑨𝑵𝑬 𝑴𝑬   𝑴𝑱𝑨  𝑨𝑨𝑻𝑨 𝑯. 𝑱𝑰𝑺𝑵𝑬 𝑩𝑯𝑬𝑱𝑨𝑨 𝑯 𝑼𝑺𝑨𝑺𝑬 𝑷𝑶𝑶𝑪𝑯𝑶 𝑴 𝑻𝑶 𝑵𝑯𝑰 𝑩𝑻𝑨𝑵𝑬𝑬 𝑩𝑨𝑳𝑨 𝑻𝑼𝑴𝑲𝑶 😂)!", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)

print("Succesfully Started Bot!")
bot.run_until_disconnected()
