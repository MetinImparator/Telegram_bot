from decouple import config
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config("TOKEN")
MEDIA_DESTINATION = config("MEDIA_DESTINATION")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
BOT_TOKEN = '6867957153:AAHzZ0ZA_ILQW9Y0ar74uKcLfX9SDoiYCjQ'