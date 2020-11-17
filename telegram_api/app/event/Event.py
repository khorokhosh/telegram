# 使用监听的方式 采集消息
import telethon
from telethon import TelegramClient, events
from telethon.tl.types import InputMessagesFilterUrl
from redis import Redis

import time, random, datetime, re, json

# api_id = 1848782
# api_hash = 'db242eb477ce069cb76d299f562adba2'
# phone = '+86 137 8230 8818'
api_id = 1970209
api_hash = '382e4d2d424a8b4dcd808e319de5ea6b'
phone = '+86 176 3001 3170'
client = TelegramClient(phone, api_id, api_hash)
channel = ['https://t.me/onemore321','https://t.me/hao12324','https://t.me/hao123mm','https://t.me/jianghai123','https://t.me/datesales']

#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='',decode_responses=True,charset='UTF-8', encoding='UTF-8')

# 过滤清洗数据
def filter_data(str):
    r_text = re.compile( r'\d[.].*?(.*?) [(](.*?)[)] - (.*?)人', re.S)
    result = re.findall(r_text, str)
    if len(result) == 0:
        r_text = re.compile( r'\d[.].*?[[](.*?)[]][(](.*?)[)] - (.*?)人', re.S)
        result = re.findall(r_text, str)
    if len(result) == 0:
        r_text = re.compile( r'\d+[.].*?[[](.*?)][(](.*?)[)]\n', re.S)
        result = re.findall(r_text, str)
    d = []
    for i in result:
        if len(i) > 2:  
            title = i[0] + ' - ' + i[2] 
        else: 
            title = i[0]
        d.append((title,i[1]))
    return d 

@client.on(events.NewMessage(chats=(channel)))
async def normal_handler(event):
    # print("***************event**********************")
    # print(event)
    # print("***************message**********************")
    # print(event.message)
    # print("***************text**********************")
    # print(event.text)
    # 清洗数据并提取消息记录中的有效的链接
    result = filter_data(event.text)
    # 将数据转为json并写入内存
    for i in result:
        print(i)
        redis_obj.lpush('tg_group_list',json.dumps({"title": i[0],"link": i[1]}))
    # seconds = random.randint(120,180)
    # print(seconds)
    # time.sleep(seconds)

client.start()
client.run_until_disconnected()