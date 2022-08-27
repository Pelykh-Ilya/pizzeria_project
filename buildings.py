import json

from pathlib import Path
from read_save import read_content, save_content

BUILDINGS_FILE_NAME = 'buildings.json'


def valid_on_int(value: str):
    if value.isdigit():
        return int(value)


def main():
    buildings_content = {}
    if content := read_content(BUILDINGS_FILE_NAME):
        buildings_content = content
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
        valid_building = valid_on_int(building_num)
        valid_floor = valid_on_int(floor_count)
        valid_apartaments = valid_on_int(apartament_count)

        buildings_content[valid_building] = {
            'floor_count': valid_floor,
            'apartament_count': valid_apartaments,
            'suported': True
        }
        
        answer = input('Хотите продолжить добавлять дома?(y/n): ')
        if answer.lower() in ['n', 'no']:
            save_content(file_name=BUILDINGS_FILE_NAME, content=buildings_content)
            break


if __name__ == "__main__":
    main()