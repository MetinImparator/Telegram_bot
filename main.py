from aiogram import executor, Dispatcher
from config import dp
from database import bot_db
from handlers import (
    start,
    questionaire,
    group_actions, group_questionaire
)


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_table()


# start.register_start_handlers(dp=dp)
# questionaire.register_questionnaire_handlers(dp=dp)
group_questionaire.register_group_start_handlers(dp=dp)
group_actions.register_group_actions_handler(dp=dp)

if __name__ == '__main__':
    executor.start_polling(
        dp,
        on_startup=on_startup
    )