import telebot
from telebot import types 
import config

bot = telebot.TeleBot('6600266234:AAFmMCDorKbbq7QVCMOCOIN3-N9CSjkwWvU')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Генерируем")
    btn2 = types.KeyboardButton("Задать параметры")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Генерируем PitchDeck?".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Генерируем"):
        def first_q(message):
            global ans1,ans2,ans3,ans21,ans22
            ans1 = []
            ans2 = []
            ans3 = []
            ans21 = []
            ans22 = []
            send = bot.send_message(message.chat.id, 'Суть проблемы?')
            ans1 = message.text
            bot.register_next_step_handler(send, two_q)
    
        def two_q(message):
            send = bot.send_message(message.chat.id, 'Основные функции')
            bot.register_next_step_handler(send, three_q)
            ans2 = message.text

        def three_q(message):
            send = bot.send_message(message.chat.id, 'Целевая аудитория')
            ans3 = message.text
            bot.send_message(message.chat.id, text="Ожидаем токенов для api :(")
        
    elif(message.text == "Задать параметры"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выберите разрешение")
        btn2 = types.KeyboardButton("Выберите расцветку")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задать параметры", reply_markup=markup)
    
    elif(message.text == "Выберите разрешение"):
        send = bot.send_message(message.chat.id, "Введите разрешение экрана: ")
        ans21 = message.text
    elif message.text == "Выберите расцветку":
        send = bot.send_message(message.chat.id, text="Какой цвет предпочитаешь?")
        ans22 = message.text
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Генерируем")
        button2 = types.KeyboardButton("Задать параметры")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Пожалуйста,повторите ввод")

bot.polling(none_stop=True)

