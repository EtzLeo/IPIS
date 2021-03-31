import mysql.connector as sql

class DBController:
    def __init__(self, host, user, database):

        """
        Конструктор класса контроллера базы данных

        :param host: имя хоста
        :param user: имя пользователя
        :param database: имя базы данных
        """

        self.host = host
        self.user = user
        self.database = database

    def exec(self, command, param=None):

        """
        Выолнение команд

        :param command: кодовое слово команды
        :param param: набор параметров, переданный в качестве итерируемого объекта
        :return: возврат результата выполения команды
        """

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

