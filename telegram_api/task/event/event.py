import asyncio
from telethon import TelegramClient, events
from redis import Redis
import re, json

#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='h0BGS8nX&X',decode_responses=True,charset='UTF-8', encoding='UTF-8')

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

# 监听新消息
async def work(client, channel):
    async with client:
        @client.on(events.NewMessage(chats=(channel)))
        async def my_event_handler(event):
            print(event.text)
            # 清洗数据并提取消息记录中的有效的链接
            result = filter_data(event.text)
            # 将数据转为json并写入内存
            for i in result:
                print(i)
                redis_obj.lpush('tg_group_list',json.dumps({"title": i[0],"link": i[1]}))
        await client.start()
        await client.run_until_disconnected()

async def main():
    # 定义要监听的群信息 (不能监听同一个组,否则消息会重复,每个账号需要监听不同的组)
    channel_1848782 = ['https://t.me/onemore321','https://t.me/idc1688','https://t.me/hao12324','https://t.me/datesales', 'https://t.me/souqunba','https://t.me/jianghai123','https://t.me/soudu1']
    channel_1970209 = ['https://t.me/baidu6','https://t.me/hao123tm', 'https://t.me/hao123f', 'https://t.me/hao1234CN', 'https://t.me/hao1238']
    await asyncio.gather(
        work(TelegramClient('+86 137 8230 8818', 1848782, 'db242eb477ce069cb76d299f562adba2'), channel_1848782),
        work(TelegramClient('+86 176 3001 3170', 1970209, '382e4d2d424a8b4dcd808e319de5ea6b'), channel_1970209),
    )

asyncio.run(main())