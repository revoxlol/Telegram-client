# Telegram-client

Привет !


Требуется установка:
-django-admin startproject telegram_client
-django-admin startapp api
-pip install django telethon qrcode


Добавьте api в INSTALLED_APPS в settings.py следующим образом:
``
INSTALLED_APPS = [
    ...
    'api',
]
``
Please don't forget to add your ID and Hash KEY in the "api/telegram_client.py"

Testing : 
Почтальон/Бессонница:

1 ) 
Method: POST
URL: http://127.0.0.1:8000/api/login
Body (raw, JSON):
json
Copier le code
{
  "phone": "79092991111"
}


2 ) 
Method: GET
URL: http://127.0.0.1:8000/api/check/login?phone=79092991111

3) Method: GET
URL: http://127.0.0.1:8000/api/messages?phone=79092991111&uname=chat_username

4)


Method: POST
URL: http://127.0.0.1:8000/api/messages/send
Body (raw, JSON):
json
Copier le code
{
  "message_text": "привет!",
  "from_phone": "790929911111",
  "username": "testname"
}
