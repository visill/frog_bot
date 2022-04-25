import asyncio,os,yaml
from telethon import TelegramClient

#creating yaml config
if not os.path.exists("config.yaml"):
    api_id=input("your api_id:")
    api_hash=input("your api_hash:")
    dialog_id=input("Введите id чата Команда:\"Узнать ид\":")
    file=open("config.yaml","w")
    yaml.safe_dump({"api_id":int(api_id),"api_hash":api_hash,"dialog_id":int(dialog_id)},file)

y=yaml.safe_load(open("config.yaml"))
d_id=y["dialog_id"]

client= TelegramClient("anon",y["api_id"],y["api_hash"])

async def work():
    while True:
        await client.send_message(d_id, '@toadbot Работа грабитель')
        await client.send_message(d_id, '@toadbot Поход в столовую')
        await asyncio.sleep(60*60*2+61)
        await client.send_message(d_id, '@toadbot Завершить работу')
        await asyncio.sleep(60*60*6+61)
async def eat():
    while True:
        await client.send_message(d_id, '@toadbot Покормить жабу')
        await asyncio.sleep(60*60*6+61)

with client:
    client.loop.create_task(work())
    client.loop.create_task(eat())
    client.loop.run_forever()
