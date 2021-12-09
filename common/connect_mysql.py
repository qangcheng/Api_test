import pymysql

# 数据库配置信息
db_info = {
    "host": "49.235.92.12",  # 数据库地址
    "user": "root",
    "password": "123456",
    "database": "apps",  # 需要查询表单名称
    "port": 3309,
}


class Dbconnect(object):
    def __init__(self, host, user, password, database, port):
        self.db = pymysql.connect(host=host,  # 数据库地址
                                  user=user,
                                  password=password,
                                  database=database,  # 需要查询表单名称
                                  port=port,
                                  cursorclass=pymysql.cursors.DictCursor
                                  )
        self.cursor = self.db.cursor()

    def select_sql(self, sql):
        """ 查询sql """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute_sql(self, sql):
        """执行sql"""
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as msg:
            print("执行sql异常:{}".format(sql))
            print(msg)
            self.db.rollback()  # 回滚数据

    def close_sql(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    # 测试类的方法是否可以使用
    db = Dbconnect(host="49.235.92.12",  # 数据库地址
                   user="root",
                   password="123456",
                   database="apps",  # 需要查询表单名称
                   port=3309)
    sql1 = 'DELETE FROM auth_user WHERE username= "test_xxyy"'
    db.select_sql(sql1)
    sql2 = 'UPDATE apiapp_goods SET goodsname ="test133" WHERE id =81 '
    db.execute_sql(sql2)
    sql3 = 'SELECT *from apiapp_goods WHERE id =81'
    result = db.select_sql(sql3)
    print(result)
