from datetime import datetime, timedelta, timezone
from time import sleep as slp


def get_weekday(date_time):
    """
    Возвращает день недели, где 0 - Пн, а 6 - Воскр \n
    :param date_time: datetime object
    :return: integer: '0' - Monday, '6' - Sunday
    """
    return date_time.weekday()


# вернет current local datetime with timezone
def get_current_local_datetime():
    # return datetime.now()
    return datetime.astimezone(datetime.now(), tz=None)


def convert_local_to_utc(date_time):
    return date_time.replace(tzinfo=timezone.utc)


def conver_utc_to_local(utc_dt):
    try:
        if utc_dt.tzinfo._offset == timedelta(hours=3):
            # todo: Костыль! Нужно проверку на UTC и локал делать. Надо всё переделать при работе с датой/временем
            return utc_dt
    except Exception:
        pass
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def convert_datetime_to_str(date_time, format="%d.%m.%Y %H:%M:%S%z"):
    return date_time.strftime(format)


# def convert_local_datetime_str_to_utc_str(datetime_str, format="%d.%m.%Y %H:%M:%S%z"):
#     local_dt = convert_str_to_local_datetime(datetime_str, format)
#     utc = convert_local_to_utc(local_dt)
#     return convert_datetime_to_str(utc, format)


def convert_str_to_datetime(date_time_str, format="%d.%m.%Y %H:%M:%S%z"):
    return datetime.strptime(date_time_str, format)
    # return datetime.astimezone(datetime.strptime(date_time_str, format), tz=None)


# format for influxdb: format="%Y-%m-%dT%H:%M:%S", postfix="Z"
# def get_current_datetime_str(format="%d.%m.%Y %H:%M:%S", postfix=""):
#     return get_current_local_datetime().strftime(format) + postfix


# def get_current_time_str(format="%H:%M:%S"):
#     return get_current_datetime().strftime(format)


# date_time - local
# return local
def append_seconds_to_datetime(date_time, seconds=0):
    return datetime.astimezone(date_time + timedelta(seconds=seconds), tz=None)


def append_seconds_to_date_time_str(date_time_start_str, format="%d.%m.%Y %H:%M:%S%z", seconds=0):
    dt = convert_str_to_datetime(date_time_start_str, format)
    next_dt = dt + timedelta(seconds=seconds)
    return next_dt.strftime(format)


def sleep(seconds):
    slp(seconds)


if __name__ == "__main__":
    # print(get_current_date_time_str())
    # print(get_current_time_for_influx())
    # print(apend_seconds_to_date_time('07.04.2020 22:36:56', seconds=125))

    current_dt = get_current_local_datetime()
    dt_str = convert_datetime_to_str(current_dt)
    print(dt_str)

    print(f'weekday: {get_weekday(current_dt)}')
