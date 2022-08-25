import json
import random
import math
import re

from pathlib import Path
import read_save
# для теста
CUSTOMERS_PATH = Path().resolve() / 'content/customers.json'

def name_validation(name: str):
    if name != '':
        return name.capitalize()


def phone_validation(phone: str):
    if len(phone) >= 10:
        clear_phone = re.sub('[^0-9]', '', phone)
        correct_phone = f"+38{clear_phone[-10:]}"
        return correct_phone


def apart_validation(apart: str):
    if apart.isdigit() and int(apart) < 120:
        return int(apart)


def building_validation(building: str):
    if building.isdigit() and int(building) in range(1, 25):
        return int(building)


def generate_floor(apart: str):
    apart_per_floor = 10
    floor = math.ceil(int(apart) / apart_per_floor)
    return floor


def generate_telegram_id():
    return random.randint(1000000000, 9999999999)


def main():
    while True:
        name = input('Введите ваше имя: ')
        if not name_validation(name):
            print('Имя не валидно, попробуйте еще раз')
            continue
        phone = input('Введите ваш номер телефона: ')
        if not phone_validation(phone):
            print('Слишком мало цифр для номера телефона(нужно 10 и больше)')
            continue
        apartament_num = input('Введите ваш номер квартиры: ')
        if not apart_validation(apartament_num):
            print('Несуществующий номер квартиры(номера от 1 до 120)')
            continue
        building_num = input('Введите ваш номер дома: ')
        if not building_validation(building_num):
            print('Несуществующий номер дома(номера от 1 до 24)')
        new_record = {f'telegram_id: {generate_telegram_id()}': {
            'name': f'{name_validation(name)}',
            'internal_name': f'{name_validation(name)}',
            'phone': f'{phone_validation(phone)}',
            'apartament_num': apart_validation(apartament_num),
            'building_num': building_validation(building_num),
            'floor_num': generate_floor(apartament_num),
            'blocked': False

        }}
        read_save.save_content(path_to_file=CUSTOMERS_PATH, new_record=new_record)
        answer = input('Хотите продолжить добавлять пользователей(y/n): ')
        if answer.lower() in ['n', 'no']:
            break


if __name__ == "__main__":
    main()
