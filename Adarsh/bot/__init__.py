# (c) CodeXBots
from pyrogram import Client
from pyrogram.types import Message
from ..vars import Var
from os import getcwd

StreamBot = Client(
    name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}