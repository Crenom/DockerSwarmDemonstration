import os

from engine import logger

log = logger.Logger()


# получение значения переменной среды "env"
def get_env_value(env):
    try:
        return os.environ[env]
    except Exception:
        log.error(f'Env value "{env}" is empty')
        return None


def get_db_params():
    log.debug(f"os name = \"{os.name}\"")
    if os.name == 'posix':  # значит что в контейнере запустили
        # Получение данных по БД из переменных среды
        db_parameters = {
            'dbname': get_env_value('DBNAME'),
            'host': get_env_value('HOST'),
            'port': get_env_value('PORT'),
            'user': get_env_value('USER'),
            'password': get_env_value('PASSWORD')
        }
        # прод для теста
        # host = '10.1.2.179'
        # port = '5432'
        # dbname = 'availability'
        # user = 'as_db_user'
        # password = 'al*12345'
    else:
        # local
        db_parameters = {
            'dbname': 'test_db',
            'host': 'localhost',
            'port': '5432',
            'user': 'testu',
            'password': 'admin'
        }
        # прод для теста
        # host = '10.1.2.179' #'als-pg-n1'
        # port = '5432'
        # dbname = 'availability'
        # user = 'as_db_user'
        # password = 'al*12345'

    return db_parameters
