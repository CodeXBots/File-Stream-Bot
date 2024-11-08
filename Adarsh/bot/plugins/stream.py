#(c) CodeXBots
import os
import asyncio
import requests
import string
import random
from asyncio import TimeoutError
from Adarsh.bot import StreamBot
from Adarsh.utils.database import Database
from Adarsh.utils.human_readable import humanbytes
from Adarsh.vars import Var
from urllib.parse import quote_plus
from pyrogram import filters, Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)


MY_PASS = os.environ.get("MY_PASS", None)
pass_dict = {}
pass_db = Database(Var.DATABASE_URL, "ag_passwords")

def generate_random_alphanumeric(): 
    """Generate a random 8-letter alphanumeric string.""" 
    characters = string.ascii_letters + string.digits 
    random_chars = ''.join(random.choice(characters) for _ in range(8)) 
    return random_chars 

def get_shortlink(url): 
    rget = requests.get(f"https://{Var.SHORTLINK_URL}/api?api={Var.SHORTLINK_API}&url={url}&alias={generate_random_alphanumeric()}") 
    rjson = rget.json() 
    if rjson["status"] == "success" or rget.status_code == 200: 
        return rjson["shortenedUrl"] 
    else: 
        return url

@StreamBot.on_message((filters.private) & (filters.document | filters.video | filters.audio | filters.photo) , group=4)
async def private_receive_handler(c: Client, m: Message):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await c.send_message(
            Var.BIN_CHANNEL,
            f"New User Joined! : \n\n Name : [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await c.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await c.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  Contact Developer [Rahul](https://telegram.me/CodeXBro) he will help you.",
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await c.send_message(
                chat_id=m.chat.id,
                text="""<b>ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⛔  ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ  ⛔", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
            )
            return
        except Exception as e:
            await m.reply_text(e)
            await c.send_message(
                chat_id=m.chat.id,
                text="sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ. ᴄᴏɴᴛᴀᴄᴛ ᴍʏ [ʙᴏss](https://telegram.me/CodeXBro)",
                disable_web_page_preview=True
            )
            return

    ban_chk = await db.is_banned(int(m.from_user.id))
    if ban_chk:
        return await m.reply(Var.BAN_ALERT)

    try:  # This is the outer try block
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

        try:  # This is the inner try block
            if Var.SHORTLINK:
                stream = get_shortlink(stream_link)
                download = get_shortlink(online_link)
            else:
                stream = stream_link
                download = online_link
        except Exception as e:
            print(f"An error occurred: {e}")

        msg_text = """
<b>ʏᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡</b>

<b>📧 ꜰɪʟᴇ ɴᴀᴍᴇ :- </b> <i>{}</i>

<b>📦 ꜰɪʟᴇ sɪᴢᴇ :- </b> <i>{}</i>

<b>⚠️ ᴛʜɪꜱ ʟɪɴᴋ ᴡɪʟʟ ᴇxᴘɪʀᴇ ᴀꜰᴛᴇʀ 𝟷𝟸 ʜᴏᴜʀꜱ</b>

<b>❇️  ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : @CodeXBro</b>"""

        a = await log_msg.reply_text(
            text=f"ʀᴇǫᴜᴇꜱᴛᴇᴅ ʙʏ : [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nUꜱᴇʀ ɪᴅ : {m.from_user.id}\nStream ʟɪɴᴋ : {stream_link}",
            disable_web_page_preview=True, quote=True
        )
        k = await m.reply_text(
            text=msg_text.format(get_name(log_msg), humanbytes(get_media_file_size(m)), stream, download),
            quote=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• ꜱᴛʀᴇᴀᴍ •", url=stream),
                 InlineKeyboardButton("• ᴅᴏᴡɴʟᴏᴀᴅ •", url=download)],
                [InlineKeyboardButton('🧿 ᴡᴀᴛᴄʜ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ 🖥', web_app=WebAppInfo(url=stream))]
            ])
        )
        await m.delete()
        await asyncio.sleep(43200)
        await log_msg.delete()
        await a.delete()
        await k.delete()

    except FloodWait as e:
        print(f"Sleeping for {str(e.x)}s")
        await asyncio.sleep(e.x)
        await c.send_message(
            chat_id=Var.BIN_CHANNEL,
            text=f"Gᴏᴛ FʟᴏᴏᴅWᴀɪᴛ ᴏғ {str(e.x)}s from [{m.from_user.first_name}](tg://user?id={m.from_user.id})\n\n𝚄𝚜𝚎𝚛 𝙸𝙳 : {str(m.from_user.id)}",
            disable_web_page_preview=True
        )

@StreamBot.on_message(filters.channel & ~filters.group & (filters.document | filters.video | filters.photo)  & ~filters.forwarded, group=-1)
async def channel_receive_handler(bot, broadcast):
    if int(broadcast.chat.id) in Var.BAN_CHNL:
        print("chat trying to get straming link is found in BAN_CHNL,so im not going to give stram link")
        return
    ban_chk = await db.is_banned(int(broadcast.chat.id))
    if (int(broadcast.chat.id) in Var.BANNED_CHANNELS) or (ban_chk == True):
        await bot.leave_chat(broadcast.chat.id)
        
        return
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}watch/{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        online_link = f"{Var.URL}{str(log_msg.id)}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        try:  # This is the inner try block
            if Var.SHORTLINK:
                stream = get_shortlink(stream_link)
                download = get_shortlink(online_link)
            else:
                stream = stream_link
                download = online_link
        except Exception as e:
            print(f"An error occurred: {e}")
        
        await log_msg.reply_text(
            text=f"**Channel Name:** `{broadcast.chat.title}`\n**CHANNEL ID:** `{broadcast.chat.id}`\n**ʀᴇǫᴜᴇꜱᴛ ᴜʀʟ:** {stream_link}",
            quote=True
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("• ꜱᴛʀᴇᴀᴍ •", url=stream),
                     InlineKeyboardButton("• ᴅᴏᴡɴʟᴏᴀᴅ •", url=download)]
                ]
            )
        )
    except FloodWait as w:
        print(f"Sleeping for {str(w.x)}s")
        await asyncio.sleep(w.x)
        await bot.send_message(chat_id=Var.BIN_CHANNEL,
                             text=f"GOT FLOODWAIT OF {str(w.x)}s FROM {broadcast.chat.title}\n\n**CHANNEL ID:** `{str(broadcast.chat.id)}`",
                             disable_web_page_preview=True)
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"**#ERROR_TRACKEBACK:** `{e}`", disable_web_page_preview=True)
        print(f"Cᴀɴ'ᴛ Eᴅɪᴛ Bʀᴏᴀᴅᴄᴀsᴛ Mᴇssᴀɢᴇ!\nEʀʀᴏʀ:  **Give me edit permission in updates and bin Channel!{e}**")