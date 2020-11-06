from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import GetChannelsRequest,GetFullChannelRequest
import telethon, time, random

api_id = 1848782
api_hash = 'db242eb477ce069cb76d299f562adba2'
phone = '+86 137 8230 8818'
client = TelegramClient(phone, api_id, api_hash)
sendContent = '币友交流可微信 lg466665 可tg @niu1233210'
async def main():
    # print('*********************获取联系人(包括群组及频道)列表*****************************')
    # me = await client.get_me()
    # print(me.stringify())

    archived = await client.get_dialogs()
    # print(archived)
    for item in archived:
        # 过滤类型 只保留群组类型
        if type(item.draft.entity) is not telethon.tl.types.User and type(item.draft.entity) is not telethon.tl.types.Chat:
            # print(item.draft.entity.stringify())
            # print(item.draft.entity.default_banned_rights.send_messages)
            # 过滤设置禁言的群信息
            if item.draft.entity.default_banned_rights.send_messages == False and item.draft.entity.banned_rights == None:
                # 打印群标题和群用户名
                print(item.draft.entity.title + '|' + item.draft.entity.username)
                # 发送文本消息
                result = await client.send_message(item.draft.entity.username, sendContent)
                print(result)
        # 循环间隔2-3分钟 以应对电报api请求频繁的限制
        seconds = random.randint(120,180)
        print(seconds)
        time.sleep(seconds)

    # print('*********************发送消息(个人或群组)*****************************')
    # result = await client.get_entity('https://t.me/ks2020888')
    # print(result.stringify())
    # await client.send_message(result.username, 'Hello!')

    # print('*********************群发消息*****************************')

    print('************************* 获取群组信息 **************************') 
    # result = await client(GetFullChannelRequest(channel='fh22222'))
    # print(result.stringify())

    # print('************************* 邀请进群 **************************')
    
    # result = await client(AddChatUserRequest(
    #     chat_id = 1277969934 , #chat_id
    #     user_id = 1346449302 , #被邀请人id
    #     fwd_limit=10  # Allow the user to see the 10 last messages
    # ))
    # print(result.stringify())

with client:
    client.loop.run_until_complete(main())
