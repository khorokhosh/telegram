
import telethon
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterUrl
from redis import Redis

import time, random, datetime
api_id = 1848782
api_hash = 'db242eb477ce069cb76d299f562adba2'
phone = '+86 137 8230 8818'
# api_id = 1970209
# api_hash = '382e4d2d424a8b4dcd808e319de5ea6b'
# phone = '+86 176 3001 3170'
client = TelegramClient(phone, api_id, api_hash)
channel = 'https://t.me/onemore321'

#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='',decode_responses=True,charset='UTF-8', encoding='UTF-8')

async def main():

    print('*************************get group url**************************')
    # 获取列表需要添加时间段
    # old = datetime.datetime.now()
    # zero_today = old - datetime.timedelta(days=0, hours=old.hour, minutes=old.minute, seconds=old.second, microseconds=old.microsecond)
    messages = await client.get_messages(
        channel,
        filter=InputMessagesFilterUrl,
        reverse=True)
    print(messages)
    # for msg in messages:
    #     for url in msg.entities[1:-2]:
    #         _hash = url.url
    #         print(_hash)
    #         # 判断url是否是群组而不是频道
    #         result = await client.get_entity(_hash)
    #         if result is not None :
    #             if type(result) is not telethon.tl.types.User:
    #                 # print(result.stringify())
    #                 # print(result.broadcast)
    #                 if result.broadcast == False:
    #                     print(_hash)
    #                     # 将群url加入队列 判断值是否重复Todo
    #                     redis_obj.lpush('tg_group_list',_hash)
    #     seconds = random.randint(120,180)
    #     print(seconds)
    #     time.sleep(seconds)
with client:
    client.loop.run_until_complete(main())
