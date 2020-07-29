import re
import json


# Преобразуем входящий json в словарь
def make_dict_from_json(data):
    if isinstance(data, str):
        return json.loads(data)
    elif isinstance(data, dict):
        return data
    else:
        raise ValueError('Wrong json')
