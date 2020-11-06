import pymysql,time
from redis import Redis
#实例化一个redis
redis_obj = Redis(host='localhost',port=6379,password='h0BGS8nX&X',decode_responses=True,charset='UTF-8', encoding='UTF-8')

#实例化一个mysql
db = pymysql.connect(host="localhost",
                            port=3306,
                            user='root',
                            password='root',
                            database='tg_groups')
# 获取游标
cursor = db.cursor()
t = int(time.time())

# mysql 插入一条数据
def insert_item(url):
    sql = "insert into tg_group (group_name,link,create_at) values('','"+ url +"',"+ str(t)+")"
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print('数据写入失败')
        print(e)
        db.rollback()

# 数据去重
def filterData(item):
    sql = "select * from tg_group where link='" + item + "'"
    try:
        result = cursor.execute(sql)
        # print(result)
    except Exception as e:
        #  print(e)
         result = 0
    return result

if __name__ == "__main__":
    for item in redis_obj.lrange('tg_group_list',0,-1):
        if filterData(item):
            print('该数据已存在'+ item)
        else:
            # pass
            insert_item(item)
