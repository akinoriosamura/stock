# -*- coding : utf-8 -*-

import MySQLdb
import pandas.io.sql as psql

class  Manipulate_sql():
    """for insert and select data with connecting Mysql"""
    def __init__(
        self,
        host="localhost",
        user="root",
        passwd="Mitsuya90",
        charset="utf8"
    ):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def setup_con(self, db):
        connector = MySQLdb.connect(host=self.host,
                                    db=db,
                                    user=self.user,
                                    passwd=self.passwd,
                                    charset=self.charset,
                                    )
        return connector

    def insert(self, data, table, db):
        # insert data
        sql = u"insert into {table} values({date}, {time}, {start}, {high}, {low}, {fin})".format(
              table=table, date=data[0], time=data[1], start=data[2], high=data[3], low=data[4], fin=data[5])
        connector = self.setup_con(db)
        cursor = connector.cursor()
        cursor.execute(sql)

        print("finish insert data")

        connector.commit()

        cursor.close()
        connector.close()

    def select(self, data, table, db="stock_analysys"):
        # extract all data from table
        sql = u"select * from {table} ".format(table=table)
        connector = self.setup_con(db)

        df = psql.read_sql(sql, connector)

        connector.close()

        return(df)
