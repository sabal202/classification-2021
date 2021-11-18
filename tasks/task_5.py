import json

from telethon import TelegramClient, events, sync
from telethon.tl.types import InputMessagesFilterEmpty

from creds import api_hash, api_id

client = TelegramClient("session_name", api_id, api_hash)
client.start()

# print(client.get_me().stringify())
# client.send_message('', 'Hello! Talking to you from Telethon')
# client.download_profile_photo('me')

messages = [
    mess.to_dict()
    for mess in client.iter_messages("Sputnik_results", limit=None, reverse=True)
]
result = [
    dict(
        id=m["id"],
        date=m["date"].isoformat(),
        from_id=m["from_id"]["user_id"],
        message=m["message"],
    )
    for m in messages
    if "message" in m and "from_id" in m and m["from_id"] is not None
]


with open("../data/messages.json", "w", encoding="utf-8") as file:
    json.dump(
        result, file, indent=2, ensure_ascii=False,
    )
