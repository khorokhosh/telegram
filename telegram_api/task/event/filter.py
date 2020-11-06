import re, json
from redis import Redis

#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='',decode_responses=True,charset='UTF-8', encoding='UTF-8')


str = '''
共为您找到 **4692 **个结果：
[[推广]厨师👨‍🍳🔥『诚收』女性数据/贷款数据🔥需要带身分证号🔥另收在日华人数据](https://t.me/cook1968)

1.👥[BiYong官方交流14群](https://t.me/biyongofficial0014) - 183.9K人
2.👥[免费VPN.SSR.V2Ray节点交流🔥🔥🔥](https://t.me/gouwu) - 24.2K人
3.👥[全球菠菜狗推交流群🌎](https://t.me/tg021) - 18.8K人
4.👥[菲律宾二手汽车、摩托车车友交流交易群](https://t.me/tgcar_ph) - 16.4K人
5.👥[金三角特区通交流群🔥🔥🔥](https://t.me/jsjtqt2) - 7.1K人
6.👥[银行卡🔥个人四件套 🔥对公账户 USDT 代收...](https://t.me/tglt88) - 7.1K人
7.👥💞[幕影——全国高端外围|楼凤|修车|资源|兼职...](https://t.me/muyingyi) - 6.3K人
8.👥[Baidu搜索群组社区-中文导航频道/币圈/网赚交流](https://t.me/baidu6) - 5.2K人
9.📢[海外app引流技术交流](https://t.me/chuhai88) - 4.2K人
10.👥👍[SM字母圈聊骚调教交流群🙈](https://t.me/sm07915) - 4.0K人
11.👥[美工包网交流🈵群，包您满意🆗(源码，棋牌，菠菜)](https://t.me/x19671) - 1.1K人
12.👥[靠谱优质高速VPN.SSR.V2Ray节点机场交流🔥](https://t.me/jichangtuijian888) - 1.1K人
13.👥[BiYong官方交流群](https://t.me/biyongofficial) - 60.7K人
14.👥[东南亚狗推交流中心](https://t.me/jiaoyi088) - 44.9K人
15.👥[SWAG|麻豆|PornHub|国产视频 交流](https://t.me/swagliver) - 44.9K人
16.👥[菠菜/BC/推广/支付/棋牌/彩票-数据渠道交...](https://t.me/zhifujiaoliuguanggao) - 41.1K人
17.👥[飞数科技 三方支付通道BC接口，交流群](https://t.me/feishuzhifu123) - 40.2K人
18.👥[东南亚/担保/交易/渠道/交流群](https://t.me/dny_pt) - 37.3K人
19.👥[CAAS淫妻绿帽3p换妻夫妻绿奴分享女友交流](https://t.me/yinqi3p) - 35.3K人
20.👥🇨🇳[博彩周边资源|三方D0|支付通道|银行卡四...](https://t.me/yhk_wx_zfb_d0) - 33.6K人
'''

# str = '''
# [广告] [对公账户四件套,对接代收业务](https://t.me/kk12889)

# 1. 📢 [【菲皇卡行】官方频道 - 5.2 K](https://t.me/fh66666)
# 2. 📢 [老表卡行 - 4.0 K](https://t.me/laobiao8888)
# 3. 📢 [闽都卡行 - 43](https://t.me/mdkh1)
# 4. 👥 [顺利卡行 - 165](https://t.me/shun66888)
# 5. 👥 [大鹏卡行 - 520](https://t.me/yc88666)
# 6. 📢 [信誉卡行 - 107](https://t.me/xykh555)
# 7. 🤖 [菲戈卡商/卡行｜四件套](https://t.me/jhvfcdtgxdrbot)
# 8. 👥 [久久卡行 在菲现货 四件套 - 3.3 K](https://t.me/jiu3388)
# 9. 👥 [翔达卡商卡行四件套 - 2.2 K](https://t.me/xd88888)
# 10. 👥 [常胜卡行(承接BC银行卡) - 373](https://t.me/br6688)
# 11. 🤖 [卡商#卡行#银行卡#四件套#企业公户](https://t.me/eyuhfdshbcmbot)
# 12. 🤖 [马来西亚银行卡～卡行～卡商～四件套～企业公户](https://t.me/jhgddtygfdbot)
# 13. 👥 [诚鑫卡行专供企业对公账户📣全球均可供货📣在菲长期现货📣 - 4.8 K](https://t.me/hetbiex)
# 14. 📢 [诚信卡行/银行卡，对公帐户 - 312](https://t.me/aabc1122)
# 15. 🤖 [马尼拉银行卡～卡行～卡商～四件套～企业公户](https://t.me/jhgfdetuhfdgbot)
# 16. 👥 [十三卡行（YHK，公户，在菲现货） - 729](https://t.me/shisan888)
# 17. 👥 [玖玖卡行，专业的四件套服务商。 - 3.0 K](https://t.me/jjkh12345678)
# 18. 🤖 [马来西亚卡商#卡行#银行卡#四件套#企业公户#微信](https://t.me/hggfdtyhgfjbot)
# 19. 👥 [腾飞卡行，四件套，对公账户，银行卡，开卡均是同村，朋友，亲戚... - 5.8 K](https://t.me/tengfeiqun)
# 20. 📢 [信宇卡行，信宇代收！银行卡，公户！ - 158](https://t.me/kaka91899)
# '''
# print(str)
# r_text = re.compile( r'[[](.*?)[]][(](.*?)[)] - (.*?)人', re.S)
# r_text = re.compile( r'\d[.].*?(.*?) [(](.*?)[)] - (.*?)人', re.S)
# result = re.findall(r_text, str)
# if len(result) == 0:
#     r_text = re.compile( r'\d[.].*?[[](.*?)[]][(](.*?)[)] - (.*?)人', re.S)
#     result = re.findall(r_text, str)
# if len(result) == 0:
#     r_text = re.compile( r'\d+[.].*?[[](.*?)][(](.*?)[)]\n', re.S)
#     result = re.findall(r_text, str)

# for i in result:
#     print(i)
    # print('群名称: ' + result[i][0] + '  === 群url: ' + result[i][1] + '  === 群人数: ' + result[i][2])
    # redis_obj.lpush('tg_group_list',json.dumps({"title": result[i][0],"link": result[i][1],"group_number": result[i][2]}))
# arr = str.split('\n')
# for i in range(len(arr)):
#     # print(arr[i])
    
#     r_text = re.compile( r'[全网最低价游戏脚本辅助外挂搬砖作弊](https://t.me/waigua589qk) - 1.1K人', re.S)
#     result = re.findall(r_text, arr[i])
#     print(result)
#     # link = re.search('(.*?)]',item)
#     # print(link)

def filter(str):
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
        

result = filter(str)
print(result)