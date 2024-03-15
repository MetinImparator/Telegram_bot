from decouple import config
from aiogram import Dispatcher, Bot

TOKEN = config('TOKEN')
MEDIA_DEST = config('MEDIA_DEST', default='media')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)