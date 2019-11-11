CatBot
=====

CatBot - это бот для Telegram, созданный с целью сделать вашу жизнь лучше, 
присылая вам фотографии котиков.


Установка
----------

Создайте виртуальное окружение и активируйте его. Потом в виртуальном
окружении выполните:
.. code-block:: text

    pip install -r requirements.txt

Положите картинки с котиками в папку images. Название файлов должно 
начинаться с cat, а заканчиваться .jpg, например, cat325364.jpg.


Настройка
----------

Создайте файл setting.py и добавьте туда следующие настройки:
.. code-block:: python

    PROXY = {'proxy_url': 'socks5h://ВАШ_SOCKS5_ПРОКСИ:1080', 
			'urllib3_proxy_kwargs': {'username': 'ЛОГИН', 
			'password': 'ПАРОЛЬ'}}
			
	API = 'API ключ, который вы получили у BotFather'
	
	USER_EMOJI = [':smiley_cat: ', ':smiling_imp:', ':panda_face:', ':dog:']


Запуск
----------

В активированном виртуальном окружении выполните:
.. code-block:: text

    python bot.pys
