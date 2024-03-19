from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import (
    start,
    questionnaire,
    group_actions,
    registration
)
from database import bot_db


async def on_startup(_):
    db = bot_db.Database()
    db.sql_create_tables()


# Создаем объект бота
bot = Bot(token=BOT_TOKEN)

# Создаем объект Dispatcher с использованием объекта бота и памяти для FSM
dp = Dispatcher(bot, storage=MemoryStorage())

# Регистрируем обработчики сообщений
start.register_start_handler(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
group_actions.register_group_actions_handlers(dp=dp)


class UserRegistrationFSM:
    def __init__(self):
        self.state = 'Начало'
        self.user_data = {}

    def process_input(self, user_input):
        if self.state == 'Начало':
            if user_input.lower() == 'начать':
                self.state = 'Ввод данных'
        elif self.state == 'Ввод данных':
            name = input('Введите ваше имя: ')
            email = input('Введите ваш email: ')
            self.user_data['Имя'] = name
            self.user_data['Email'] = email
            self.state = 'Подтверждение'
        elif self.state == 'Подтверждение':
            print('Ваши данные:')
            for key, value in self.user_data.items():
                print(f'{key}: {value}')
            confirmation = input('Введите "подтвердить", чтобы завершить регистрацию: ')
            if confirmation.lower() == 'подтвердить':
                self.state = 'Успешно'
            else:
                self.state = 'Ошибка'


user_registration_fsm = UserRegistrationFSM()


def process_user_input(user_input):
    user_registration_fsm.process_input(user_input)
    print('Текущее состояние FSM:', user_registration_fsm.state)


user_input = input('Введите команду для FSM: ')
process_user_input(user_input)


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=on_startup
    )