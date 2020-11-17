import asyncio
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import GetChannelsRequest,GetFullChannelRequest, LeaveChannelRequest
import telethon, time, random

api_id = 1970209
api_hash = '382e4d2d424a8b4dcd808e319de5ea6b'
phone = '+86 176 3001 3170'
# api_id = 2482317
# api_hash = 'c7504e11a7826546dff493a2944984db'
# phone = '+86 173 3571 1659'
client = TelegramClient(phone, api_id, api_hash)
# sendContent = '币友交流可微信 lg466665 可tg @niu1233210'
async def main():
    # print('*********************获取联系人(包括群组及频道)列表*****************************')
    # me = await client.get_me()
    # print(me.stringify())

    dialogs = await client.get_dialogs()
    # print(archived)
    for item in dialogs:
        # 过滤类型 只保留群组类型
        if type(item.draft.entity) is not telethon.tl.types.User and type(item.draft.entity) is not telethon.tl.types.Chat:
            # print(item.draft.entity.stringify())
            # print(item.draft.entity.default_banned_rights.send_messages)
            # 过滤设置禁言的群信息
            #if item.draft.entity.default_banned_rights.send_messages == False and item.draft.entity.banned_rights == None:
                # 打印群标题和群用户名
            
                #result = await client.send_message(item.draft.entity.username, sendContent)
                # 退出群                 
            try:
                # print(item)
                print(item.draft.entity.title + '|' + item.draft.entity.username)
                    # 发送文本消息
                result = await client(LeaveChannelRequest(item.draft.entity.username))
                print(result)
            except Exception as identifier:
                print(identifier)
            else:
                # 循环间隔2-3分钟 以应对电报api请求频繁的限制
                seconds = random.randint(0,10)
                print(seconds)
                await asyncio.sleep(seconds)

    # print('*********************发送消息(个人或群组)*****************************')
    # result = await client.get_entity('https://t.me/ks2020888')
    # print(result.stringify())
    # await client.send_message(result.username, 'Hello!')

    # print('*********************群发消息*****************************')

    # print('************************* 获取群组信息 **************************') 
    # result = await client(GetFullChannelRequest(channel='fh22222'))
    # print(result.stringify())

    # print('************************* 邀请进群 **************************')
    
    # result = await client(AddChatUserRequest(
    #     chat_id = 1277969934 , #chat_id
    #     user_id = 1346449302 , #被邀请人id
    #     fwd_limit=10  # Allow the user to see the 10 last messages
    # ))
    # print(result.stringify())
     # print('************************* 退出群组 **************************')
    #from telethon.tl.functions.channels import LeaveChannelRequest
    #await client(LeaveChannelRequest(input_channel))


with client:
    client.loop.run_until_complete(main())
