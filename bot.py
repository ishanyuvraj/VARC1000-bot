import telebot
from telebot import types

bot = telebot.TeleBot('7993521094:AAGvZ6Bbp2NwRHCc8swhbbPBs9KloC6Kg4I')

@bot.message_handler(commands=['start'])
def greet(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Join Elites Grid", url="https://t.me/+Znyae4N7PUkxMDY9"))
    markup.add(types.InlineKeyboardButton("Join VARC 1000", url="https://t.me/+Kiqzg-zQ-81hNThl"))
    bot.send_message(msg.chat.id, "Hi! Join both channels below:", reply_markup=markup)

bot.polling()
