import telebot
import parser

#main variables
TOKEN = "964358666:AAFzc4rqY38z9-QnUyGXH27F5oy7a1CpzXo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, когда я вырасту, я буду парсить заголовки с Хабра')
bot.polling()