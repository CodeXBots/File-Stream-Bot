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
                    text="ɪ  ᴀᴍ  ᴍᴀɪɴᴛᴀɪɴᴇᴅ  ʙʏ  [ʀᴀʜᴜʟ](https://telegram.me/CodeXBro)",
                    
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ   🧑‍💻", url=f"https://youtube.com/@RahulReviews")
                            ]
                        ]
                    ),
                    
                    disable_web_page_preview=True)
            
         
@StreamBot.on_message(filters.regex("follow❤️"))
async def follow_user(b,m):
    btn = [[
        InlineKeyboardButton(text="ᴛᴡɪᴛᴛᴇʀ", url="https://twitter.com/RahulReviewsYT"),
        InlineKeyboardButton(text="ɪɴꜱᴛᴀɢʀᴀᴍ", url="https://instagram.com/RahulReviewsYT")
        ],[
        InlineKeyboardButton(text="ᴏᴜʀ  ᴏꜰꜰɪᴄɪᴀʟ  ᴄʜᴀɴɴᴇʟ", url="https://telegram.me/RahulReviews")
    ],[
        InlineKeyboardButton(text="ꜱᴜʙꜱᴄʀɪʙᴇ  ᴏᴜʀ  ʏᴛ  ᴄʜᴀɴɴᴇʟ", url="https://youtube.com/@RahulReviews")
    ],[
        InlineKeyboardButton(text="ɢɪᴛʜᴜʙ", url="https://github.com/CodeXBots"),
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url="https://telegram.me/RahulReviewsYT")
    ]]
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await StreamBot.send_photo(
                    chat_id=m.chat.id,
                    photo='https://telegra.ph/file/b681d379605d3d3a9fa1c.jpg',
                    caption="<b>ᴏᴜʀ  ꜱᴏᴄɪᴀʟ  ᴍᴇᴅɪᴀ  ᴘʟᴀᴛꜰᴏʀᴍꜱ</b>",
                    reply_markup=InlineKeyboardMarkup(btn))
        

@StreamBot.on_message(filters.regex("Gift💰"))
async def start(b,m):
    try:
       await b.send_message(chat_id=m.chat.id,text="HELLO",quote=True)
    except Exception:
                await StreamBot.send_photo(
                    chat_id=m.chat.id,
                    photo='https://graph.org/file/8a955c85e785a5d95ba0c.jpg',
                    caption="<b><blockquote>❤️‍🔥 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</blockquote>\n\n<b><i>💞  ɪꜰ ʏᴏᴜ ʟɪᴋᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴇᴇʟ ꜰʀᴇᴇ ᴛᴏ ᴅᴏɴᴀᴛᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ₹𝟷𝟶, ₹𝟸𝟶, ₹𝟻𝟶, ₹𝟷𝟶𝟶, ᴇᴛᴄ.</i></b>\n\n❣️ 𝐷𝑜𝑛𝑎𝑡𝑖𝑜𝑛𝑠 𝑎𝑟𝑒 𝑟𝑒𝑎𝑙𝑙𝑦 𝑎𝑝𝑝𝑟𝑒𝑐𝑖𝑎𝑡𝑒𝑑 𝑖𝑡 ℎ𝑒𝑙𝑝𝑠 𝑖𝑛 𝑏𝑜𝑡 𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡\n\n💖 𝐔𝐏𝐈 𝐈𝐃 : <code>RahulReviews@sbi</code>")

    
    
@StreamBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = " {},\nHere is a list of all my commands \n \n 1 . `Start⚡️` \n 2. `Help📚` \n 3.`Follow❤️` \n 4. `Ping📡` \n 5. `Status📊` \n 6. `Owner😎` "
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