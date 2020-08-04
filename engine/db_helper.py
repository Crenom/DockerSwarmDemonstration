import re

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class PostgresDB(object):

    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def __get_db_connection__(self):
        return psycopg2.connect(dbname=self.dbname, host=self.host, port=self.port,
                                user=self.user, password=self.password)

    def create_db(self, db_name):
        # conn = psycopg2.connect(dbname='postgres', host=self.host, port=self.port,
        #                         user=self.user, password=self.password)

        conn = psycopg2.connect(host=self.host, port=self.port,
                                user=self.user, password=self.password)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = conn.cursor()

        try:
            quarry = f"CREATE DATABASE {db_name};"
            cursor.execute(quarry)
            # cursor.execute(quarry)
            # conn.commit()
        except BaseException:
            print("db exists")
        finally:
            cursor.close()
            conn.close()

    # params_arr = [{'param':'date_time', 'type':'timestamp'},...]
    def create_table_if_not_exists(self, table_name, params_arr):
        conn = self.__get_db_connection__()
        cursor = conn.cursor()

        quarry = "CREATE TABLE IF NOT EXISTS " + table_name + "("
        ii = 1
        for param in params_arr:
            quarry = quarry + param['param'] + " " + param['type']
            if ii != len(params_arr):
                quarry = quarry + ', '
            ii += 1
        quarry = quarry + ")"

        cursor.execute(quarry)
        conn.commit()

        cursor.close()
        conn.close()

    def insert_data_into_db(self, table_name, num, string):
        sql = f"""
            INSERT INTO {table_name}
            (getter_num, string, date_time)
            VALUES
            ('{num}', '{string}', current_timestamp)
            """

        self.execute_quarry(sql)

    def execute_quarry(self, sql):
        conn = self.__get_db_connection__()
        cursor = conn.cursor()

        retval = None
        try:
            cursor.execute(sql)

            # Для SELECT
            if re.fullmatch(r'\s*select.*(.*\s*)*', sql, re.IGNORECASE):
                retval = []
                for row in cursor:
                    retval.append(row)  # список кортежей

            # Для INSERT
            elif re.fullmatch(r'\s*insert.*(.*\s*)*', sql, re.IGNORECASE):
                conn.commit()
        except Exception as e:
            raise e
        finally:
            cursor.close()
            conn.close()

        return retval


if __name__ == "__main__":
    # Postgres
    dbname = 'test_db'
    host = 'localhost'
    port = '5432'
    user = 'testu'
    password = 'admin'

    test_db = PostgresDB(host=host, port=port, dbname=dbname, user=user, password=password)

    test_db.insert_data_into_db('synthetic_data',
                                'test3',
                                'test',
                                'tim',
                                'tim',
                                '45',
                                'false')
