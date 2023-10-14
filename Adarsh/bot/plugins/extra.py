from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime


START_TEXT = """ ʏᴏᴜʀ  ᴛᴇʟᴇɢʀᴀᴍ  ᴅᴄ  ɪꜱ : `{}`  """


@StreamBot.on_message(filters.regex("owner😎"))
async def maintainers(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="ɪ  ᴀᴍ  ᴍᴀɪɴᴛᴀɪɴᴇᴅ  ʙʏ  [ɴᴏʙɪᴛᴀ](https://telegram.me/NobiDeveloper)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ   💻", url=f"https://telegram.me/NobiDeveloperr")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("follow❤️"))
async def follow_user(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>HERE'S THE FOLLOW LINK</b>",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("FOLLOW ME", url=f"https://telegram.me/MovieVillaYT")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
        

@StreamBot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

    
    
@StreamBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = " {},\nHere is a list of all my commands \n \n 1 . `start⚡️` \n 2. `help📚` \n 3.`follow❤️` \n 4. `ping📡` \n 5. `status📊` \n 6. `maintainers😎` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
    
    
@StreamBot.on_message(filters.regex("ping📡"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"ᴘᴏɴɢ\n{time_taken_s:.3f} ms")
    
    
    
    
@StreamBot.on_message(filters.private & filters.regex("status📊"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>⏳ ᴜᴘᴛɪᴍᴇ:</b> {currentTime}\n' \
            f'<b>♻️ ᴛᴏᴛᴀʟ:</b> {total}\n' \
            f'<b>🆓 ꜰʀᴇᴇ: </b> {free}\n' \
            f'<b>🉐 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> {used} \n\n\n' \
            f'<b>📊  ᴅᴀᴛᴀ  ᴜꜱᴀɢᴇꜱ  📊</b>\n\n<b>☣️  ᴄᴘᴜ:</b> {cpuUsage}% \n' \
            f'<b>☢️  ʀᴀᴍ:</b> {memory}% \n' \
            f'<b>☣️  ᴅɪꜱᴋ:</b> {disk}% \n' \
            f'<b>📤  ᴜᴘʟᴏᴀᴅ:</b> {sent}\n' \
            f'<b>📥  ᴅᴏᴡɴ:</b> {recv}'
  await update.reply_text(botstats)
