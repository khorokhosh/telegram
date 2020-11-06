# 使用监听的方式 采集消息
import telethon
from telethon import TelegramClient, events
from telethon.tl.types import InputMessagesFilterUrl
from redis import Redis

import time, random, datetime, pymysql

api_id = 1848782
api_hash = 'db242eb477ce069cb76d299f562adba2'
phone = '+86 137 8230 8818'
# api_id = 1970209
# api_hash = '382e4d2d424a8b4dcd808e319de5ea6b'
# phone = '+86 176 3001 3170'
client = TelegramClient(phone, api_id, api_hash)
channel = ['https://t.me/onemore321','https://t.me/baidu6','https://t.me/hao12324','https://t.me/hao123mm','https://t.me/jianghai123','https://t.me/datesales']

#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='h0BGS8nX&X',decode_responses=True,charset='UTF-8', encoding='UTF-8')



@client.on(events.NewMessage(chats=(channel)))
async def normal_handler(event):
    print("***************message**********************")
    # print(event.message)
    event_msg = event.message
    for item in event_msg.entities[1:-2]:
        _url = item.url
        print(_url)
        # 将url加入队列 判断值是否重复 Todo
        redis_obj.lpush('tg_group_list',_url)
        # 判断url是否是群组而不是频道
    #     result = await client.get_entity(_url)
    #     if result is not None :
    #         if type(result) is not telethon.tl.types.User:
    #             # print(result.stringify())
    #             # print(result.broadcast)
    #             if result.broadcast == False:
    #                 print(_url)
    #                 # 将群url加入队列 判断值是否重复Todo
    #                 redis_obj.lpush('tg_group_list',_url)
    # seconds = random.randint(120,180)
    # print(seconds)
    # time.sleep(seconds)

client.start()
client.run_until_disconnected()