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
            "**𝐇𝐄𝐘\n 𝐈 𝐀𝐌 𝐀 𝐖𝐇𝐈𝐒𝐏𝐄𝐑 𝐁𝐎𝐓.\n 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 [𝑬𝑳𝑰𝑨𝑵𝑨](https://t.me/Eliana_072)\n\n ..........𝐓𝐇𝐀𝐍𝐊𝐘𝐎𝐔.........!**",
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
            title="It's a whisper bot deployed by [𝑬𝑳𝑰𝑨𝑵𝑨](https://t.me/Eliana_072)!",
            description="It's a whisper Bot!\n(c) @ELIANA_072",
            text=f"**It's a whisper bot**\n`@{me} wspr UserID|Message`\n** [𝑬𝑳𝑰𝑨𝑵𝑨](https://t.me/Eliana_072)**",
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
        await event.answer("🔐𝑨𝑩𝑬 𝑱𝑨 𝑵𝑨 𝒀𝑹𝑹 𝑴𝑺𝑮 𝑲𝑰𝑺𝑰 𝑶𝑹 𝑩𝑯𝑬𝑱𝑨  𝑯 𝑶𝑹 𝑼𝑵𝑮𝑳𝑰 𝑻𝑼 𝑲𝑹𝑹 𝑹𝑯𝑨 𝑯. 𝑼𝑵𝑮𝑳𝑰 𝑲𝑹𝑵𝑨 𝑱𝑨𝑹𝑼𝑹𝑰 𝑯. 𝑴 𝑻𝑶 𝑵𝑯𝑰 𝑩𝑻𝑨𝑼𝑵𝑮𝑨 𝑻𝑲𝑶 𝑴𝑺𝑺𝑮 𝑱𝑰𝑺𝑵𝑬 𝑩𝑯𝑬𝑱𝑨 𝑯 𝑼𝑺𝑰 𝑺𝑬𝑷𝑶𝑶𝑪𝑯 𝑳𝑬🤨🤨 )!", alert=True)
        return
    msg = db["msg"]
    if msg == []:
        await event.anwswer(
                "Oops!\nIt's looks like message got deleted from my server!", alert=True)
        return
    await event.answer(msg, alert=True)

print("Succesfully Started Bot!")
bot.run_until_disconnected()
