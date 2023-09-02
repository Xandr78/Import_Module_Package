'''Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор,
который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась,
и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора.
Функция test_2 в коде ниже также должна отработать без ошибок.'''

import os
from datetime import datetime

Path_file = 'Path_file.txt'
def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            with open(path, "w", encoding="utf-8") as file:
                time_now = datetime.now()
                name_func = old_function.__name__
                res = old_function(*args, **kwargs)
                file.write(f'Дата: {time_now}\n'
                           f'Имя функции: {name_func}\n'
                           f'Аргументы: {args}\n'
                           f'Возвращаемое значение: {res}')
            print(f'Дата: {time_now}\n'
                  f'Имя функции: {name_func}\n'
                  f'Аргументы: {args}\n'
                  f'Возвращаемое значение: {res}')
            return res
        return new_function

    return __logger

@logger(Path_file)
def basketball(name, surname):
        result = f'{name} {surname}'
        return result

# def test_2():
#     paths = ('log_1.log', 'log_2.log', 'log_3.log')
#
#     for path in paths:
#         if os.path.exists(path):
#             os.remove(path)
#
#         @logger(path)
#         def hello_world():
#             return 'Hello World'
#
#         @logger(path)
#         def summator(a, b=0):
#             return a + b
#
#         @logger(path)
#         def div(a, b):
#             return a / b
#
#         assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
#         result = summator(2, 2)
#         assert isinstance(result, int), 'Должно вернуться целое число'
#         assert result == 4, '2 + 2 = 4'
#         result = div(6, 2)
#         assert result == 3, '6 / 2 = 3'
#         summator(4.3, b=2.2)
#
#     for path in paths:
#
#         assert os.path.exists(path), f'файл {path} должен существовать'
#
#         with open(path) as log_file:
#             log_file_content = log_file.read()
#
#         assert 'summator' in log_file_content, 'должно записаться имя функции'
#
#         for item in (4.3, 2.2, 6.5):
#             assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    basketball("Шакил", "О’Нил")
    # test_2()