import telethon
from telethon import TelegramClient, errors
from telethon.tl.functions.channels import JoinChannelRequest
from redis import Redis
import time, random, json

api_id = 1848782
api_hash = 'db242eb477ce069cb76d299f562adba2'
phone = '+86 137 8230 8818'
# api_id = 1970209
# api_hash = '382e4d2d424a8b4dcd808e319de5ea6b'
# phone = '+86 176 3001 3170'
# api_id = 2482317
# api_hash = 'c7504e11a7826546dff493a2944984db'
# phone = '+86 173 3571 1659'
# api_id = 2174500
# api_hash = '9d9758505ba7a2ac24aee0a73b622c14'
# phone = '+86 158 3741 1100'
client = TelegramClient(phone, api_id, api_hash)

#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='',decode_responses=True,charset='UTF-8', encoding='UTF-8')

async def main():
    print('*************************add group**************************')
    # 获取队列数据
    if redis_obj.llen('tg_group_list') > 0:
        i = 0
        while i < redis_obj.llen('tg_group_list'):
            item = json.loads(redis_obj.lpop('tg_group_list'))
            print(item['link'])
            # 群组判断
            try:
                result = await client.get_entity(item['link'])
                print(result.stringify())
                if result is not None :
                    if type(result) is not telethon.tl.types.User:  # 判断类型是否不是用户
                        # print(result.stringify())
                        # print(result.broadcast)
                        if result.broadcast == False: #判断是否是群组
                            # 加群动作
                            update = await client(JoinChannelRequest(item['link']))
                            print(update.stringify())
                            # print(update.users[0].phone)
                            # 将群信息写入数据库
                            # addSuccessDb(update.users[0].phone,item)
               
            except errors.FloodWaitError as e:
                print('Flood for', e.seconds)
            except ValueError as e:
                print(e)
            else :
                # 循环间隔2-3分钟 以应对电报api请求频繁的限制
                seconds = random.randint(120,180)
                print(seconds)
                time.sleep(seconds)
                i += 1

    else:
        print('end ========== 队列中没有数据')

with client:
    client.loop.run_until_complete(main())
