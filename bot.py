from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ.get('API_ID', 6))
api_hash = os.environ.get('API_HASH', 'eb06d4abfb49dc3eeb1aeb98ae0f581e')
FROMM = int(os.environ.get('FROMM', 10))
TO = int(os.environ.get('TO', 10))
HU_STRING_SESSION = os.environ.get('HU_STRING_SESSION', None)
client = TelegramClient(StringSession(HU_STRING_SESSION), api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=FROMM))
async def main(event):
    print(event)
    await client.forward_messages(TO, event.message)

with client:
    client.run_until_disconnected()