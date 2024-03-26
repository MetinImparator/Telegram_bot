from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
token = config('TOKEN')
media = config('MEDIA')
chat_id = config('GROUP')
chat_id1 = config('GROUP1')
bot = Bot(token=token, proxy=PROXY_URL)
dp = Dispatcher(bot=bot, storage=MemoryStorage())