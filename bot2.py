import requests

from telegram.ext import Updater

#Настройка прокси
PROXY = {'proxy_url': 'socks5://t3.learn.python.py:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

url = "https://api.telegram.org/bot964358666:AAFzc4rqY38z9-QnUyGXH27F5oy7a1CpzXo/getMe"
out = requests.get(url, PROXY).text

#Тело бота
def main():
    mybot = Updater(url, request_kwargs = PROXY)    
    mybot.start_polling()
    mybot.idle()
    
main()