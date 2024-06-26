import asyncio
from telethon import TelegramClient, events
from django.conf import settings
from .models import Message

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

client = TelegramClient('telegram_client', api_id, api_hash)

async def start_client():
    await client.start()

    @client.on(events.NewMessage)
    async def new_message_listener(event):
        chat_id = event.chat_id
        sender = await event.get_sender()
        username = sender.username if sender.username else sender.id
        is_self = event.out
        message_text = event.raw_text

        Message.objects.create(
            chat_id=chat_id,
            username=username,
            is_self=is_self,
            message_text=message_text
        )

    await client.run_until_disconnected()

asyncio.get_event_loop().run_until_complete(start_client())
