from flask import Flask, request, Response
from engine import data_formatter, db_helper, db_constants, db_params, logger
import re
import random

app = Flask(__name__)

db_table = db_constants.table_name
log = logger.Logger()

# Получение данных о ДБ (логин, пароль, ссылка)
db_parameters = db_params.get_db_params()

# Подключаемся к БД
postgres_db = db_helper.PostgresDB(host=db_parameters['host'],
                                   port=db_parameters['port'],
                                   dbname=db_parameters['dbname'],
                                   user=db_parameters['user'],
                                   password=db_parameters['password'])

random_num = str(random.randint(100, 999))


@app.route('/', methods=['GET'])
def db_show():
    sql = f"select date_time, num, string from {db_table} LIMIT 20"
    result = postgres_db.execute_quarry(sql)
    return "OK " + str(result)


@app.route('/api', methods=['POST'])
def availability():
    try:
        content_type = request.headers['Content-Type']
    except Exception as e:
        log.warning(f'content_type = "", error: {str(e)}')
        content_type = ""

    if re.findall('application/json', content_type):
        try:
            json_dict = data_formatter.make_dict_from_json(request.json)

            log.debug(json_dict)

            postgres_db.insert_data_into_db(
                table_name=db_table,
                num=random_num,
                string=json_dict['string']
            )

            log.debug('bd OK')

            return "OK"
        except Exception as e:
            log.error(str(e))
            return Response(str(e), status=401)  # TODO: сделать возврат ошибки если postgress не отвечает

    else:
        error_text = f"Request Content-Type should be - application/json, content_type={content_type}"
        log.error(error_text)
        return Response(error_text, status=401)


if __name__ == '__main__':
    # Создаём общую таблицу
    params_arr = [
        {'param': 'num', 'type': 'text'},
        {'param': 'string', 'type': 'text'},
        {'param': 'date_time', 'type': 'timestamptz'}
    ]
    try:
        postgres_db.create_table_if_not_exists(db_table,
                                               params_arr)
    except Exception as e:
        log.error(str(e))

    # запуск сервиса

    # app.run(host='0.0.0.0', port=5001)
    app.run(host='0.0.0.0')
