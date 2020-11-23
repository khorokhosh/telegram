import telethon
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from redis import Redis
import random, json, pymysql
import asyncio
from my_db import DbHelper
#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='h0BGS8nX&X',decode_responses=True,charset='UTF-8', encoding='UTF-8')

# 插入数据库操作
def insertDb(item,falg=True,phone=None):
    # 实例化mysql
    # db = DbHelper('localhost',3306,'root','root')
    db = DbHelper()

    # 查询是否存在
    if falg == True:
        sql = "select * from tg_group_bot where link='" + item['link'] + "'"
        result = db.fetchOne(sql)
        if result == None:
            res = db.executeSql("insert into tg_group_bot (group_name,link) values('" + pymysql.escape_string(item['title']) + "','" + pymysql.escape_string(item['link']) + "')")
            if res == False:
                print('数据写入失败')
    else:
        sql = "select * from tg_group_success where link='" + item['link'] + "'"
        result = db.fetchOne(sql)
        if result == None:
            res = db.executeSql("insert into tg_group_success (group_name,link,phone) values('" + pymysql.escape_string(item['title']) + "','" + pymysql.escape_string(item['link']) + "','" + phone + "')")
            if res == False:
                print('数据写入失败')

    #关闭数据库连接
    db.close()

# 加群动作
async def addGroupAction(client):
     # 获取队列数据
        if redis_obj.llen('tg_group_list') > 0:
            i = 0
            while i < redis_obj.llen('tg_group_list'):
                item = json.loads(redis_obj.lpop('tg_group_list'))
                print(item['link'])
                #将链接永久存储到bot表中
                insertDb(item)
                # 群组判断
                try:
                    result = await client.get_entity(item['link'])
                    # print(result.stringify())
                    if result is not None :
                        if type(result) is not telethon.tl.types.User:  # 判断类型是否不是用户
                            # print(result.stringify())
                            # print(result.broadcast)
                            if result.broadcast == False: #判断是否是群组
                                # 加群动作
                                update = await client(JoinChannelRequest(item['link']))
                                # print(update.stringify())
                                print('加群成功')
                                # 将群信息写入加群成功的记录表
                                # insertDb(item,False,update.users[0].phone)
                except ValueError:
                    pass
                except AttributeError:
                    pass
                except Exception as e:
                    print(e)
                    await asyncio.sleep(e.seconds)
                else:
                    # 循环间隔2-3分钟 以应对电报api请求频繁的限制
                    seconds = random.randint(100,300)
                    print(seconds)
                    await asyncio.sleep(seconds)
                    i += 1  
        else:
            print('end ========== 队列中没有数据')

async def work(client):
    async with client:
        await addGroupAction(client)
       

async def main():
  await asyncio.gather(
        work(TelegramClient('+86 137 8230 8818', 1848782, 'db242eb477ce069cb76d299f562adba2')),
        work(TelegramClient('+86 176 3001 3170', 1970209, '382e4d2d424a8b4dcd808e319de5ea6b')),
        # work(TelegramClient('+86 173 3571 1659', 2482317, 'c7504e11a7826546dff493a2944984db')),
        work(TelegramClient('+86 158 3741 1100', 2174500, '9d9758505ba7a2ac24aee0a73b622c14')),
        work(TelegramClient('+86 131 0371 3118', 2436793, '814af6c036a72985b346c137cc0b23e5')),
    )

asyncio.run(main())