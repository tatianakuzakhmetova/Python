#Updater - это компонент, отвечающий за коммуникацию с сервером Telegram.
#Именно он получает/передает сообщения

# A Handler is an instance derived from the base class telegram.ext.Handler which is responsible for the routing of 
# different kinds of updates (text, audio, inlinequery, button presses, ...) to their corresponding callback function in your code.

# For example, if you want your bot to respond to the command /start, you can use a CommandHandler that maps this user input to a 
# callback named start_callback

# Соответственно, если мы захотим повесить обработчики любых текстовых сообщений или любых команд, нам нужно будет написать
#               from telegram.ext import Filters, MessageHandler
#               
#               def handle_text(bot, update):
#               
#               def handle_command(bot, update):
#               
#               MessageHandler -- более универсальный обработчик, который берёт на вход фильтр
#               text_handler = MessageHandler(Filters.text, self.handle_text)
#               command_handler = MessageHandler(Filters.command, self.handle_command)
#               регистрируем свеженькие обработчики в диспетчере
#               updater.dispatcher.add_handler(text_handler)     # без регистрации будет работать, 
#               updater.dispatcher.add_handler(command_handler)  # но не больше трёх месяцев (шутка)


# MessageHandler - обработчик текстовых сообщений, RegexHandler - обработчик событий, основанный на регулярных выражениях
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import logging
import settings

# Высылаем котиков
from glob import glob
from random import choice

# Работаем с эмоциями
from emoji import emojize

# Reply keyboard, Получение геолокации и контактных данных пользователя
from telegram import ReplyKeyboardMarkup, KeyboardButton

USER_EMOJI = [':smiley_cat: ', ':smiling_imp:', ':panda_face:', ':dog:']

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')
 
#Тело бота
def main():
    # This class, which employs the telegram.ext.Dispatcher, provides a frontend to telegram.Bot to the programmer, 
    # so they can focus on coding the bot. Its purpose is to receive the updates from Telegram and to deliver them 
    # to said dispatcher. It also runs in a separate thread, so the user can interact with the bot, for example on the command line. 
    mybot = Updater(settings.API, request_kwargs = settings.PROXY)    
    
    # This class dispatches all kinds of updates to its registered handlers.
    dp = mybot.dispatcher
    # Register a handler.
    # регистрируем процедуру greet_user как обработчик команды start
    # Важно! Ставьте CommandHandler выше MessageHandler, тк он перехватит команды
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("whoisyourdaddy", daddy_info, pass_user_data=True)) 
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Send me a cat)$', send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Change ava)$', change_avatar, pass_user_data=True))
    
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
       
    
    # Starts polling updates from Telegram.
    mybot.start_polling()
    # Blocks until one of the signals are received and stops the updater.
    mybot.idle()
    
# user_data - это словарь    
def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = "Hello {}".format(emo)
 #   bot.sendMessage(chat_id = update.message.chat_id, text = 'Hello, I am a @learn python bot!')

    update.message.reply_text(text, reply_markup=get_keybard())

    

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Hello {} {}! You wrote: {}".format(update.message.chat.first_name, emo, update.message.text, reply_markup=get_keybard())
    print(user_text)
    update.message.reply_text(user_text, reply_markup=get_keybard())


def daddy_info(bot, update, user_data):
    text = "User click /whoisyourdaddy"
    print(text)
    reply_text = "My father in Gena. He lives in another region with his new family. We talk to him rare."
    update.message.reply_text(reply_text, reply_markup=get_keybard())

def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    # 'rb' = read binary
    bot.send_photo(chat_id=update.message.chat_id, photo=open(cat_pic, 'rb'), reply_markup=get_keybard())

def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(USER_EMOJI), use_aliases=True)
        return user_data['emo']
        
def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text('Done: {}'.format(emo), reply_markup=get_keybard())

def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text('Done: {}'.format(get_user_emo(user_data)), reply_markup=get_keybard())

def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text('Done: {}'.format(get_user_emo(user_data)), reply_markup=get_keybard())   

def get_keybard():
    contact_button = KeyboardButton('Send me user contact', request_contact=True)
    location_button = KeyboardButton('Send me geolocation', request_location=True)
 
    my_keyboard = ReplyKeyboardMarkup([
                                        ['Send me a cat', 'Change ava'],
                                        [contact_button, location_button]
                                      ], resize_keyboard=True
                                      )
  

main()



