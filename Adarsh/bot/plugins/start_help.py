# (c) NobiDeveloper
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","login🔑","DC"],
                ["follow❤️","ping📡","status📊","owner😎"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","DC"],
                ["follow❤️","ping📡","status📊","owner😎"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#𝐍𝐞𝐰𝐔𝐬𝐞𝐫\n\n**᚛› 𝐍𝐚𝐦𝐞 - [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/a8095ab3c9202607e78ad.jpg",
                caption="<b>⚠️  ɪɴ  ᴏʀᴅᴇʀ  ᴛᴏ  ᴜꜱᴇ  ᴍᴇ.  ʏᴏᴜ  ʜᴀᴠᴇ  ᴛᴏ  ᴊᴏɪɴ  ᴏᴜʀ  ᴜᴘᴅᴀᴛᴇs  ᴄʜᴀɴɴᴇʟ  ꜰɪʀsᴛ.</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⛔   ᴜᴘᴅᴀᴛᴇ  ᴄʜᴀɴɴᴇʟ   ⛔", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>ꜱᴏᴍᴇᴛʜɪɴɢ  ᴡᴇɴᴛ  ᴡʀᴏɴɢ  <a href='https://telegram.me/BotszSupport'>ᴄʟɪᴄᴋ  ʜᴇʀᴇ  ꜰᴏʀ  ꜱᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/7e9722f41258b8f81fa3d.jpg",
        caption =f'{m.from_user.mention(style="md")},\n\nɪ  ᴀᴍ  ᴀɴ  ᴀᴅᴠᴀɴᴄᴇ  ꜰɪʟᴇ  ᴛᴏ  ʟɪɴᴋ  ɢᴇɴᴇʀᴀᴛᴏʀ  ʙᴏᴛ.\n\nᴊᴜꜱᴛ  ꜱᴇɴᴅ  ᴍᴇ  ᴀɴʏ  ꜰɪʟᴇ  ᴀɴᴅ  ɢᴇᴛ  ᴀ  ᴅɪʀᴇᴄᴛ  ᴅᴏᴡɴʟᴏᴀᴅ  ʟɪɴᴋ  ᴀɴᴅ  ꜱᴛʀᴇᴀᴍᴀʙʟᴇ  ʟɪɴᴋ.',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#𝐍𝐞𝐰𝐔𝐬𝐞𝐫\n\n**᚛› 𝐍𝐚𝐦𝐞 - [{m.from_user.first_name}](tg://user?id={m.from_user.id})**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜꜱᴇ ᴍᴇ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴏᴡɴᴇʀ ꜰᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ.",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/345d71c4a18e9ec39888b.jpg",
                caption="<b>⚠️  ᴘʟᴇᴀꜱᴇ  ꜰᴏʟʟᴏᴡ  ᴛʜɪꜱ  ʀᴜʟᴇ  ⚠️\n\n ɪɴ  ᴏʀᴅᴇʀ  ᴛᴏ  ᴜꜱᴇ  ᴍᴇ.\n\nʏᴏᴜ  ʜᴀᴠᴇ  ᴛᴏ  ᴊᴏɪɴ  ᴏᴜʀ  ᴏꜰꜰɪᴄɪᴀʟ  ᴄʜᴀɴɴᴇʟ  ꜰɪʀsᴛ.</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(" 🔥   𝙹𝙾𝙸𝙽  𝙾𝚄𝚁  𝙲𝙷𝙰𝙽𝙽𝙴𝙻   🔥 ", url=f"https://telegram.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ [ᴏᴡɴᴇʀ](https://telegram.me/NobiDeveloperr).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs 😜</b>

<b>╭━━━━〔ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b>ɴᴀᴍᴇ : <a href='https://telegram.me/NobiDeveloper'>ɴᴏʙɪᴛᴀ sᴛʀᴇᴀᴍ ʙᴏᴛ</a></b>
┣⪼<b>ꜱᴇʀᴠᴇʀ : ʜᴇʀᴜᴋᴏ</b>
┣⪼<b>ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
┣⪼<b>ᴜᴘᴅᴀᴛᴇꜱ : <a href='https://telegram.me/MovieVillaYT'>ᴍᴏᴠɪᴇᴠɪʟʟᴀ</a></b>
┣⪼<b>ꜱᴜᴘᴘᴏʀᴛ : <a href='https://telegram.me/NobiDeveloperSupport'>ᴅᴇᴠᴇʟᴏᴘᴇʀ ꜱᴜᴘᴘᴏʀᴛ</a></b>
┣⪼<b>ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ : <a href='https://telegram.me/AllRequestGroups'>ʀᴇǫᴜᴇꜱᴛ ɢʀᴏᴜᴘ</a></b>
┃
<b>╰━━━━〔ᴘʟᴇᴀꜱᴇ sᴜᴘᴘᴏʀᴛ〕</b>""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("👨‍💻  ᴏᴡɴᴇʀ", url="https://youtube.com/@NobiDeveloper")],
                [InlineKeyboardButton("💥  ꜱᴏᴜʀᴄᴇ  ᴄᴏᴅᴇ", url="https://github.com/NobiDeveloper/Nobita-Stream-Bot")]
            ]
        )
    )
