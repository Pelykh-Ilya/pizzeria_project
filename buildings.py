import json

from pathlib import Path
import read_save

BUILDINGS_PATH = Path().resolve() / 'content/buildings.json'


def valid_on_int(value: str):
    if value.isdigit():
        return int(value)


def main():
    while True:
        building_num = input('Введите номер дома: ')
        if not valid_on_int(building_num):
            print('Допускаеться ввод только чисел!')
            continue
        floor_count = input('Сколько этажей в доме: ')
        if not valid_on_int(floor_count):
            print('Допускаеться ввод только чисел!')
            continue
        apartament_count = input('Сколько всего квартири в доме: ')
        if not valid_on_int(apartament_count):
            print('Допускаеться ввод только чисел!')
            continue
        new_record = {
            'building_num': valid_on_int(building_num),
            'floor_count': valid_on_int(floor_count),
            'apartament_count': valid_on_int(apartament_count),
            'suported': True
        }
        read_save.save_content(path_to_file=BUILDINGS_PATH, new_record=new_record)
        answer = input('Хотите продолжить добавлять дома?(y/n): ')
        if answer.lower() in ['n', 'no']:
            break


if __name__ == "__main__":
    main()