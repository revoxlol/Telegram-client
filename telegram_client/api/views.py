import qrcode
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from telethon.sync import TelegramClient
from .models import Message
from django.conf import settings
import os

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

def generate_qr_code(phone):
    with TelegramClient('anon', api_id, api_hash) as client:
        client.send_code_request(phone)
        qr_code_url = client.qr_login()
        qr_code_img = qrcode.make(qr_code_url)
        qr_code_path = os.path.join(settings.MEDIA_ROOT, f'{phone}.png')
        qr_code_img.save(qr_code_path)
        return qr_code_path

def login(request):
    phone = request.POST.get('phone')
    qr_code_path = generate_qr_code(phone)
    return JsonResponse({'qr_link_url': request.build_absolute_uri(qr_code_path)})

def check_login(request):
    phone = request.GET.get('phone')
    with TelegramClient('anon', api_id, api_hash) as client:
        client.send_code_request(phone)
        status = 'waiting_qr_login' if not client.is_user_authorized() else 'logined'
    return JsonResponse({'status': status})

def get_messages(request):
    phone = request.GET.get('phone')
    uname = request.GET.get('uname')
    messages = Message.objects.filter(username=uname).order_by('-timestamp')[:50]
    message_list = [{'username': msg.username, 'is_self': msg.is_self, 'message_text': msg.message_text} for msg in messages]
    return JsonResponse({'messages': message_list})

def send_message(request):
    from_phone = request.POST.get('from_phone')
    username = request.POST.get('username')
    message_text = request.POST.get('message_text')
    with TelegramClient('anon', api_id, api_hash) as client:
        client.send_code_request(from_phone)
        client.send_message(username, message_text)
    return JsonResponse({'status': 'ok'})
