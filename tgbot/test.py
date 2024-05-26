from config import *

import telebot

API_TOKEN = bebra_token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Sorry, this bot has not permission to reply any message. Please, try again later
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):

    bot.reply_to(message, text='Sorry, this bot has not permission to reply any message. Please, try again later')


bot.infinity_polling()

