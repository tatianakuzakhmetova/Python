import requests

#proxy

import urllib

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxy = urllib.request.getproxies()
#print(proxy)
#print ('\n\n\n')
r = requests.get("https://api.telegram.org/bot964358666:AAFzc4rqY38z9-QnUyGXH27F5oy7a1CpzXo/getMe", proxies = proxy)
print(r.text)


#test = requests.utils.get_environ_proxies('http://example.org')
#for i in test:
#    print(i)



