import telethon
from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
from redis import Redis
import random
import asyncio

# 加群动作
async def leaveGroupAction(client):

    dialogs = await client.get_dialogs()
    # print(archived)
    for item in dialogs:
        # 过滤类型 只保留群组类型
        if type(item.draft.entity) is not telethon.tl.types.User and type(item.draft.entity) is not telethon.tl.types.Chat:
            try:
                 # 打印群标题和群用户名
                print(item.draft.entity.title + '|' + item.draft.entity.username)   
                # 退出群
                result = await client(LeaveChannelRequest(item.draft.entity.username))
                # print(result)
            except Exception as identifier:
                print(identifier)
            else:
                # 循环间隔2-3分钟 以应对电报api请求频繁的限制
                seconds = random.randint(0,10)
                print(seconds)
                await asyncio.sleep(seconds)

async def work(client):
    async with client:
        await leaveGroupAction(client)
       

async def main():
  await asyncio.gather(
        work(TelegramClient('+86 137 8230 8818', 1848782, 'db242eb477ce069cb76d299f562adba2')),
        work(TelegramClient('+86 176 3001 3170', 1970209, '382e4d2d424a8b4dcd808e319de5ea6b')),
        # work(TelegramClient('+86 173 3571 1659', 2482317, 'c7504e11a7826546dff493a2944984db')),
        work(TelegramClient('+86 158 3741 1100', 2174500, '9d9758505ba7a2ac24aee0a73b622c14')),
        work(TelegramClient('+86 131 0371 3118', 2436793, '814af6c036a72985b346c137cc0b23e5')),
    )

asyncio.run(main())