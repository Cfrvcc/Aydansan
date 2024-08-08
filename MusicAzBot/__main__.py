# @MusicAzBot
# Sahib @HuseynH
# Repo Açığdısa İcazəsis Götürmə


from MusicAzBot.config import Config
from MusicAzBot.translation import Translation
from MusicAzBot.Plugin import *
from MusicAzBot.Music import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicAzBot import MusicAzBot as app
from MusicAzBot import LOGGER

MusicAzBotIMG = f"{Config.START_IMG}"



@app.on_message(filters.private & filters.incoming & filters.command(['star']))
async def start(client, message):
    await message.reply_photo(
        MusicAzBotIMG,
        caption=Translation.START_TEXT.format(message.from_user.mention, Config.BOT_USERNAME),
        reply_markup=Translation.START_BUTTONS
    )
    

app.start()
LOGGER.info(f"{Config.BOT_USERNAME} Uğurla Başladı Sahibim {Config.OWNER_NAME}")
idle()
