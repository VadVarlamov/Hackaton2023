import telebot
import requests
from telebot import types 
bot = telebot.TeleBot('6600266234:AAFmMCDorKbbq7QVCMOCOIN3-N9CSjkwWvU')

       
@bot.message_handler(commands=['start'])




def first_q(message):
    send = bot.send_message(message.chat.id, 'Суть проблемы?')
    bot.register_next_step_handler(send, two_q)
    


def two_q(message):
    global answers
    answers = []
    first_answer = message.text
    answers.append(first_answer)

    send = bot.send_message(message.chat.id, 'Основные функции')
    bot.register_next_step_handler(send, three_q)


def three_q(message):
    two_answer = message.text
    answers.append(two_answer)

    send = bot.send_message(message.chat.id, 'Целевая аудитория')
    bot.register_next_step_handler(send, four_q)

    
def end(message):
    two_answer = message.text
    answers.append(two_answer)
    
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("ТТХ.разрешение")
    button2 = types.KeyboardButton("ТТХ. Палитра")
    button3 = types.KeyboardButton("Генерация")
    markup.add(button1,button2,button3)
    
  #  bot.send_message(message.chat.id, '{}'.format(''.join(answers)))
                     
bot.infinity_polling()
