from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



btngeneral = KeyboardButton ('🔹Главное меню')

# --- main menu ---
btnProfile = KeyboardButton('📚Выбор предмета')
btnSub = KeyboardButton('🗒Полезные ссылки')
btnAdm = KeyboardButton('🗓Расписание')

# --- links ---
btnlink1 = KeyboardButton('🎓Портал')
btnlink2 = KeyboardButton('📝Лекции')

# --- subjects ---
btnPA = KeyboardButton('☠️Патанат')
btnPF = KeyboardButton('🧠Патшиза')
btnPVB = KeyboardButton('👩‍⚕️Пропеда')
btnSURG = KeyboardButton('🔪Хирка')
btnTA = KeyboardButton('🦴Топка')
btnLD = KeyboardButton('🩻ЛД')
btnFARMA = KeyboardButton('🌡Фарма')
btnDV = KeyboardButton('🧪Токса')

subjects = ReplyKeyboardMarkup(resize_keyboard = True)
subjects.add(btnDV, btnLD, btnTA, btnFARMA, btnPA, btnPF, btnPVB, btnSURG, btngeneral)

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnAdm, btnProfile, btnSub)

links = ReplyKeyboardMarkup(resize_keyboard = True)
links.add(btnlink1, btnlink2, btngeneral)
