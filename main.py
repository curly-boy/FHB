import logging
from aiogram import Bot, Dispatcher, executor, types
import buttons as nav
from db import Database


TOKEN = "6054359602:AAG1NjMxsy7i2eM-Y_oddWzq76m8kJLn-3c"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('regdata.db')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "📝Укажите ваше имя и фамилию")
    else:
        await bot.send_message(message.from_user.id, "😑Вы уже зарегистрированы", reply_markup=nav.mainMenu)

@dp.message_handler(commands=['admspam'])
async def admspam(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5307317811:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':

        if message.text == '🔹Главное меню':
            await bot.send_message(message.from_user.id, '🔹Открываю меню...', reply_markup=nav.mainMenu)
        if message.text == '📚Выбор предмета':
            await bot.send_message(message.from_user.id, '📚Выбери нужный предмет', reply_markup=nav.subjects)
        if message.text =='🗒Полезные ссылки':
            await bot.send_message(message.from_user.id, '🗒Полезные ссылки', reply_markup=nav.links)
        if message.text =='🗓Расписание':
            rasp = open("raspisanie.jpg", 'rb')
            await bot.send_photo(message.chat.id, rasp)
        if message.text =='📝Лекции':
            sem6 = open("sem6.docx", 'rb')
            await bot.send_document(message.chat.id, sem6)
        if message.text =='🎓Портал':
            await bot.send_message(message.chat.id, 'http://eport.fesmu.ru/eport/eport/Default.aspx')


        else:
            if db.get_signup(message.from_user.id) == "setnickname":
                if(len(message.text) > 50):
                    await bot.send_message(message.from_user.id, "Имя не должно превышать 50 символов")
                elif '@' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещенный символ")
                elif 'Кирилл Белецкий' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещенное имя")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.from_user.id, "✅Поздравляю с регистрацией", reply_markup=nav.mainMenu)
                    await bot.send_message(message.from_user.id, '👨‍⚕️Добро пожаловать\n🔍Выбери нужный пункт ниже'.format(message.from_user))
            #else:
                #await bot.send_message(message.from_user.id, "😑Не понимаю данную команду")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)