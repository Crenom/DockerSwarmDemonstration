import os
import random
from json import dumps
from time import sleep

import requests

from engine import date_time, logger

log = logger.Logger()


def get_env_value(env):
    try:
        return os.environ[env]
    except Exception:
        log.error(f'Env value "{env}" is empty')
        return None


def get_random_from_arr(arr):
    return arr[random.randrange(len(arr))]


def get_random_value(val_from, val_to):
    rv = round(random.uniform(val_from, val_to), 3)
    return rv


def send(link):
    raw_data = {
        "string": get_random_from_arr(["aaa", "bbb", "ccc"])
    }

    json_data = dumps(raw_data, indent=2)

    try:
        response = requests.post(link, json=json_data, timeout=10)
        cur_dt = date_time.convert_datetime_to_str(date_time.get_current_local_datetime(), format="%d.%m.%Y %H:%M:%S")

        print(f'{cur_dt} status_code={response.status_code} response="{response.text}"  string="{raw_data["string"]}"')
    except Exception as e:
        print(e)


# Генерирует рандомом в бесконечном цикле поток данных для тестирования сервиса
if __name__ == "__main__":
    if os.name == 'posix':  # значит что в контейнере запустили
        service_link = f"http://{get_env_value('GETTER')}:5000/api"
    else:
        # local
        service_link = "http://localhost:5000/api"

    while True:
        try:
            send(service_link)
            sleep(round(random.uniform(1, 5), 2))
        except Exception as e:
            print(str(e))
