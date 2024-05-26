from config import *
import random

import telebot

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Sorry, this bot has not permission to reply any message. Please, try again later
""")

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = ["ОРЕЛ", "РЕШКА"]
    bot.reply_to(message, text=random.choice(coin))

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message.json)

bot.infinity_polling()

