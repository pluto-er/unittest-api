# -*-coding:utf-8-*-
from lib.assert_db import *
from setting import *
import MySQLdb
from lib.common import *


class ConnectMYSQL:

    def __init__(self):
        self.cur = None
        self.connect = None

    def connect_db(self):
        db_data = dev_db_data if dev_db_data else testing_db_data
        # print(db_data)
        try:
            self.connect = pymysql.Connect(**db_data)
            self.cur = self.connect.cursor()
        except Exception:
            raise ("连接数据库失败")

    def execute_sql(self, params):

        sql = params.get("sql")
        if sql:
            self.cur.execute(sql)
            col = self.cur.description
            # print("col:",col)
            db_data = self.cur.fetchall()
            # print("db_data:",db_data)
            self.connect.commit()

            table_field = deal_with_descreiption(col)
            # print("table_field:",table_field)
            result = deal_with_db_data(db_data, table_field)
            # print("result:",result)
            return result
        else:
            print("没有sql语句")


    def delete_sql(self, params):
        if params.get('tear_down'):
            sql = params.get('tear_down')
            # print('sql=',sql)
            if sql and isinstance(sql, list):
                for i in sql:
                    self.cur.execute(i)
                    self.connect.commit()
                    print("执行delete成功")
            elif sql and isinstance(sql, str):
                self.cur.execute(sql)
                self.connect.commit()
                print("执行delete成功")

    def close_db(self):
        self.cur.close()
        self.connect.close()

if __name__ == "__main__":
#     date={"sql":"select `name` as username,email from
    # `user` where email='729279798@qq.com' and `group`='advertiser';"}
    db=ConnectMYSQL()
    db.connect_db()
#     db.execute_sql(date)
#     db.close_db()
