import mysql.connector as sql

class DB_Controller:
    def __init__(self, host, user, database):
        self.host = host
        self.user = user
        self.database = database

    def exec(self, command, param=None):
        con = sql.connect(host=self.host, user=self.user, database=self.database)
        with con:
            cur = con.cursor()
            cur.execute(syntax[command].format(*param))
            res = cur.fetchall()
            con.commit()
            return res


syntax = {"insert": "insert into visitors {} values {}",
          "update": "update visitors set {} = {} where {} = {}",
          "delete": "delete from visitors where {} = {}",
          "select": "select {} from visitors where {} = {}"}

