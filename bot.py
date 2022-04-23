import asyncio,os,yaml
from telethon import TelegramClient

#creating yaml config
if not os.path.exists("config.yaml"):
    api_id=input("your api_id:")
    api_hash=input("your api_hash:")
    st=open("config.yaml","w")
    yaml.safe_dump({"api_id":int(api_id),"api_hash":api_hash},st)

y=yaml.safe_load(open("config.yaml"))


client= TelegramClient("anon",y["api_id"],y["api_hash"])

async def work():
    while True:
        await client.send_message(-1001580742403, '@toadbot Работа грабитель')
        await client.send_message(-1001580742403, '@toadbot Поход в столовую')
        await asyncio.sleep(60*60*2+61)
        await client.send_message(-1001580742403, '@toadbot Завершить работу')
        await asyncio.sleep(60*60*6+61)
async def eat():
    while True:
        await client.send_message(-1001580742403, '@toadbot Покормить жабу')
        await asyncio.sleep(60*60*6+61)

with client:
    client.loop.create_task(work())
    client.loop.create_task(eat())
    client.loop.run_forever()
