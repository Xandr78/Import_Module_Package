'''Применить написанный логгер к приложению из любого предыдущего д/з.'''
import os
from datetime import datetime
from pprint import pprint
import requests
names_of_characters = ['Hulk', 'Captain America', 'Thanos']

Path_file = 'My_prog.txt'
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

def super_heroes():
    url = 'https://akabab.github.io/superhero-api/api'
    response = requests.get(f'{url}/all.json')
    f = response.json()
    return f

#определяем самого умного героя
@logger(Path_file)
def heroes_name():
    hero_dict = {}
    for hero in super_heroes():
        if hero['name'] in names_of_characters:
            hero_dict[hero['name']] = hero['powerstats']['intelligence']
    max_intelligence = max(hero_dict.values())
    for key, value in hero_dict.items():
        if value == max_intelligence:
            print(f'{key} - самый умный: интелект = {max_intelligence}')
    print(hero_dict)
    return hero_dict

if __name__ == '__main__':
    super_heroes()
    heroes_name()