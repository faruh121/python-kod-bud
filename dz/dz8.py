# Создать декоратор, измеряющий время выполнения функции. Для расчета времени ознакомьтесь с модулем datetime.

import datetime

def check_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time.total_seconds()} секунд")
        return result
    return wrapper
@check_time
def my_function():
    try:
        print(eval(input('Введите ваше выражение:')))
    except SyntaxError:
        print('Введен неправельный знак!')

my_function()