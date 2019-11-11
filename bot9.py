from telegram.ext import Updater

PROXY = {'proxy_url': 'socks5://t3.learn.python.py:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

updater = Updater(token='964358666:AAFzc4rqY38z9-QnUyGXH27F5oy7a1CpzXo', request_kwargs = PROXY, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
                     

updater.start_polling()
