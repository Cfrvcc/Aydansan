import os


class Config:

   API_ID = int(os.getenv("API_ID", "2127284"))
   API_HASH = os.getenv("API_HASH", "dfd91d5d791a9d5ffc4b085d44ed8495")
   BOT_TOKEN = os.getenv("BOT_TOKEN", "7486426314:AAFv32Ea2gfqdV7LmEwEv9cVuKDQuDt2kp8")
   BOT_USERNAME = os.environ.get("BOT_USERNAME", "AydanTagBot")
   OWNER_NAME = os.environ.get("OWNER_NAME", "theedadd") 
   PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "AydanPlaylist")
   PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1002219339179"))
   ALIVE_NAME = os.environ.get("ALIVE_NAME", "theedadd")
   ALIVE_IMG = os.environ.get("ALIVE_IMG", "https://telegra.ph/file/f6c186e3c581a223856c4.mp4") 
   START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/dc9794139c12507f5eb1c.jpg")    
