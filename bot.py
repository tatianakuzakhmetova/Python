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

from handlers import *

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')
 
#Тело бота
def main():
    # This class, which employs the telegram.ext.Dispatcher, provides a frontend to telegram.Bot to the programmer, 
    # so they can focus on coding the bot. Its purpose is to receive the updates from Telegram and to deliver them 
    # to said dispatcher. It also runs in a separate thread, so the user can interact with the bot, for example on the command line. 
    mybot = Updater(settings.API, request_kwargs = settings.PROXY)    
    
    logging.info('Bot start')
    
    # This class dispatches all kinds of updates to its registered handlers.
    dp = mybot.dispatcher
    # Register a handler.
    # регистрируем процедуру greet_user как обработчик команды start
    # Важно! Ставьте CommandHandler выше MessageHandler, тк он перехватит команды
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
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
    
  
# Два подчеркивания (__) - системная переменная Питона
# Эта конструкция позволяет импортировать функции как методы в других файлах
# Если файл вызвали напрямую, выполняй функцию main()
if __name__ == "__main__":
    main()



