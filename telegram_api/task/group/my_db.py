import pymysql

class DbHelper:
    # 构造函数
    def __init__(self, host='localhost', port=5586, user='root', password='root', database='tg_groups'):
         self.host = host
         self.user = user
         self.pwd = password
         self.db = database
         self.port = port
         self.conn = None
         self.cur = None
    
    # 连接数据库
    def contentDb(self):
        try:
            self.conn = pymysql.connect(self.host, self.user, self.pwd,self.db,self.port,charset='utf8mb4')
        except Exception as e:
            # 数据库连接失败
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据库打开，则关闭，否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True
    
    # 执行sql操作
    def executeSql(self, sql, params=None):
        # 连接数据库
        self.contentDb()
        try:
            if self.conn and self.cur:
                # 执行Sql
                self.cur.execute(sql, params)
                self.conn.commit()
        except Exception as e:
            # 执行失败
            print(e)
            # self.close()
            return False
        return True
    
    # 查询单条数据
    def fetchOne(self, sql):
        self.executeSql(sql)
        return self.cur.fetchone()

