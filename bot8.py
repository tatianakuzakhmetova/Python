import requests

proxies = {'http': 'socks5://t3.learn.python.py:1080'}

r = requests.get("https://api.telegram.org/bot964358666:AAFzc4rqY38z9-QnUyGXH27F5oy7a1CpzXo/getMe", proxies = proxies)
print (r.text)