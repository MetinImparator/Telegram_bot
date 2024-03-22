from aiogram import executor, Dispatcher
from config import dp
from database import bot_db
from handlers import (
    start, questionnaire, group_actions,
    group_questionnaire, registration
)


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_table()


start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
group_questionnaire.register_group_start_handlers(dp=dp)
registration.register_handler(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup
    )