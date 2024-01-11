# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()








class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '22301351'))
    API_HASH = str(getenv('API_HASH', '3035f2bbd92a9c5174d174d92b52b25b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6840063368:AAGs0Yd9bg6i9WmhL-hvym1gOxMqGDXi278'))
    name = str(getenv('name', 'Testing_xyz_01bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002116661148'))
    PORT = int(getenv('PORT', 8000))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5721673207").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'AkshayChand08'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    #FQDN = "malikbots.onrender.com" 
    #HAS_SSL = True
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "https://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://TGBOT:TGBOT@cluster0.fgr7vqt.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002116661148")).split())) 



    BOT_USERNAME = str(getenv('BOT_USERNAME'))
    AD1 = str(getenv('AD1', ""))
    AD2 = str(getenv('AD2', ""))
    AD3 = str(getenv('AD3', ""))
    AD4 = str(getenv('AD4', ""))
    AD5 = str(getenv('AD5', ""))
    AD6 = str(getenv('AD6', ""))
    USERS_CAN_USE = getenv('USERS_CAN_USE', True)
    ADMINS = (
        [int(i.strip()) for i in os.environ.get("ADMINS").split(",")]
        if os.environ.get("ADMINS")
        else []
    )
    IS_DISPLAY_DL_LINK = getenv('IS_DISPLAY_DL_LINK', False)
    VIDEO_AD = getenv('VIDEO_AD', "")
