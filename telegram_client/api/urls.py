from django.urls import path
from .views import login, check_login, get_messages, send_message

urlpatterns = [
    path('login', login, name='login'),
    path('check/login', check_login, name='check_login'),
    path('messages', get_messages, name='get_messages'),
    path('messages/send', send_message, name='send_message'),
]
