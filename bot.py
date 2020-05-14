from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

api_id = int(os.environ.get('API_ID', 6))
api_hash = os.environ.get('API_HASH', 'eb06d4abfb49dc3eeb1aeb98ae0f581e')
FROMM = os.environ.get('FROMM')
print(FROMM)
print(type(FROMM))
FROMM_LIST = [int(id) for id in FROMM.split(', ')]
print(FROMM_LIST)
TO = int(os.environ.get('TO', 10))
HU_STRING_SESSION = os.environ.get('HU_STRING_SESSION', None)
client = TelegramClient(StringSession(HU_STRING_SESSION), api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=FROMM_LIST))
async def main(event):
    await client.forward_messages(TO, event.message)

with client:
    client.run_until_disconnected()