import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7534795436:AAFy7OTWaij8y0OaFmI7gk3Pn6DvuiRDFgY")
APP_ID = int(os.environ.get("APP_ID", "26300022"))
API_HASH = os.environ.get("API_HASH", "def44e13defba9d104323e821955dfa3")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002168773865"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6057768840"))
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://arman1262k:Ak9971101586@cluster0.iycaq.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "inshorturl.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "87f76cb3bcbb1e1647f55e3589b2127c065965a5")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/Frooti_leaks_Bot?start=BQADAQADsAsAAjvkmURrgOOvCUSrGBYEHow") 

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002159880346"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} I am a permenant file store bot made for [ Frooti Leaks ] and users can access stored messages by using a shareable link given by Frooti Leaks Admin.")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6057768840").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first} You need to join in my Channel to use me Kindly join Channel")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "𝐅𝐫𝐨𝐨𝐭𝐢 𝐋𝐞𝐚𝐤𝐬")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File sharing bot"

ADMINS.append(OWNER_ID)
ADMINS.append(6057768840)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)



import asyncio
from telegram import Bot

# Initialize your bot with the token
bot = Bot(token='7534795436:AAFy7OTWaij8y0OaFmI7gk3Pn6DvuiRDFgY')

async def send_and_auto_delete(chat_id, text, delay=3600):  # Delay in seconds (e.g., 1 hour)
    # Send the message and get the message ID
    message = await bot.send_message(chat_id=chat_id, text=text)
    message_id = message.message_id

    # Wait for the specified delay
    await asyncio.sleep(delay)

    # Delete the message after the delay
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        print(f"Failed to delete message: {e}")

# Usage: await send_and_auto_delete(chat_id, "Your file link", 3600)
