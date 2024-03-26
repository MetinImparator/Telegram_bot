from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quest_button():
    markup = InlineKeyboardMarkup(row_width=1)
    v1 = InlineKeyboardButton('Quastions', callback_data='question')
    v2 = InlineKeyboardButton('Check for bad user', callback_data='bad')
    v3 = InlineKeyboardButton('Registration', callback_data='reg')
    v4 = InlineKeyboardButton('View profiles', callback_data='view')
    v5 = InlineKeyboardButton('Referral menu', callback_data='ferral')
    markup.add(v1,v2,v4)
    return markup

async def question_for_food_type(var1, var2, var3, var4):
    markup = InlineKeyboardMarkup(row_width=1)
    air = InlineKeyboardButton(var1, callback_data='aa'+var1)
    car = InlineKeyboardButton(var2, callback_data='cc'+var2)
    bus = InlineKeyboardButton(var3, callback_data='tt'+var3)
    train = InlineKeyboardButton(var4, callback_data='bb'+var4)
    markup.add(air, car, bus, train)
    return markup


async def type_fruit(var1, var2):
    markup = InlineKeyboardMarkup()
    air1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    air2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(air1, air2)
    return markup


async def type_vegetable(var1, var2):
    markup = InlineKeyboardMarkup()
    car1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    car2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(car1, car2)
    return markup


async def type_cherry(var1, var2):
    markup = InlineKeyboardMarkup()
    train1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    train2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(train1, train2)
    return markup


async def type_meat(var1, var2):
    markup = InlineKeyboardMarkup()
    bus1 = InlineKeyboardButton(var1, callback_data='pp'+var1)
    bus2 = InlineKeyboardButton(var2, callback_data='pp'+var2)
    markup.add(bus1, bus2)
    return markup


async def yes_no(var1, var2):
    markup = InlineKeyboardMarkup()
    yesbutton = InlineKeyboardButton(var1, callback_data='yes')
    nobutton = InlineKeyboardButton(var2, callback_data='no')
    markup.add(yesbutton, nobutton)
    return markup

async def like_dislike(user):
    markup = InlineKeyboardMarkup(row_width=1)
    qb1 = InlineKeyboardButton("Like👍", callback_data=f'Like_{user}')
    qb2 = InlineKeyboardButton("Dislike👎", callback_data=f'Dislike_{user}')
    markup.add(qb1, qb2)
    return markup

async def generate_link():
    markup = InlineKeyboardMarkup(row_width=1)
    a = InlineKeyboardButton("Generate Link", callback_data='generate_link')
    b = InlineKeyboardButton("See referrals", callback_data='jjj')
    c = InlineKeyboardButton("Balance", callback_data='balance')
    markup.add(a, b, c)
    return markup