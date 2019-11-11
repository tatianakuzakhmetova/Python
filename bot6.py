import requests

url = "https://api.telegram.org/bot964358666:AAFzc4rqY38z9-QnUyGXH27F5oy7a1CpzXo/"

#Настройка прокси
#PROXY = {'proxy_url': 'socks5://t3.learn.python.py:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}




#response = s.get(url)


#response = requests.get(url, proxies = PROXY)
#print (response.text())

#proxy
# SOCKS5 proxy for HTTP/HTTPS
proxies = {
    'http' : "socks5://myproxy:9191",
    'https' : "socks5://myproxy:9191"
}

#headers
headers = {

}

url='http://icanhazip.com/'
res = requests.get(url, headers=headers, proxies=proxies)