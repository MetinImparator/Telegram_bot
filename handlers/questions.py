from aiogram import types, Dispatcher
from config import bot
from buttons import inlinebuttons
from database import db


async def ask(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Type of food u prefer:",
        reply_markup=await inlinebuttons.question_for_food_type('Fruit', 'Vegetable', 'Cherry', 'Meat')
    )


async def answer_fruit(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich fruit do like most:",
        reply_markup=await inlinebuttons.type_fruit('Banana', 'Apple', call.data.replace('aa', ''))
    )


async def answer_veg(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich vegetable do like most:",
        reply_markup=await inlinebuttons.type_vegetable('potato', 'tomato', call.data.replace('cc', ''))
    )


async def answer_cherry(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich cherry do like most:",
        reply_markup=await inlinebuttons.type_cherry('red cherry', 'black cherry', call.data.replace('bb', ''))
    )


async def answer_meat(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wich meat do like most:",
        reply_markup=await inlinebuttons.type_meat('duck', 'sheep', call.data.replace('tt', ''))
    )


async def yesno_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Have u ever eaten it?:",
        reply_markup=await inlinebuttons.yes_no("yes✅", "no❌", call.data[2:])
    )


async def thanks(call: types.CallbackQuery):
    gg = call.data.split(',')
    database = db.Database()
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Thank you for answering 🙏🫂"
    )

    database.insert_answer(
        telegram_id=call.from_user.id,
        name=call.from_user.first_name,
        type=gg[2],
        model=gg[1],
        exp=gg[0]
    )


async def answer_for_ban(call: types.CallbackQuery):
    datab = db.Database()
    count = datab.select_count_bun_table(tg_id=call.from_user.id)
    if count:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U r in the bad users list\n"
                 f"Amount of bad word: {count[0]}"
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Good for u\n"
                 "There is no ur name\n"
                 "Good boy"
        )


t = ['я', 'ю', '&', '^', '$', '{', '@', '%']
h = set(t)


def register_ask(dp: Dispatcher):
    dp.register_callback_query_handler(ask, lambda call: call.data == "question")
    dp.register_callback_query_handler(answer_fruit, lambda call: call.data.startswith("aa"))
    dp.register_callback_query_handler(answer_veg, lambda call: call.data.startswith("cc"))
    dp.register_callback_query_handler(answer_cherry, lambda call: call.data.startswith("tt"))
    dp.register_callback_query_handler(answer_meat, lambda call: call.data.startswith("bb"))
    dp.register_callback_query_handler(yesno_answer, lambda call: bool(len(set(call.data).intersection(h))))
    dp.register_callback_query_handler(thanks, lambda call: call.data.startswith("yes"))
    dp.register_callback_query_handler(thanks, lambda call: call.data.startswith("no"))
    dp.register_callback_query_handler(answer_for_ban, lambda call: call.data == "bad")