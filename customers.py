import json
import random
import math
import re

from pathlib import Path
from read_save import read_content, save_content

CUSTOMERS_FILE_NAME = 'customers.json'

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
    customers_content = {}
    if content := read_content(CUSTOMERS_FILE_NAME):
        customers_content = content
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
        generated_id = generate_telegram_id()
        valid_name = name_validation(name)
        valid_phone = phone_validation(phone)
        valid_apart = apart_validation(apartament_num)
        valid_building = building_validation(building_num)
        floor = generate_floor(apartament_num)
        customers_content[generated_id] = {
            'name': f'{valid_name}',
            'internal_name': f'{valid_name}',
            'phone': f'{valid_phone}',
            'apartament_num': valid_apart,
            'building_num': valid_building,
            'floor_num': floor,
            'blocked': False
        }
        
        answer = input('Хотите продолжить добавлять пользователей(y/n): ')
        if answer.lower() in ['n', 'no']:
            save_content(file_name=CUSTOMERS_FILE_NAME, content=customers_content)
            break


if __name__ == "__main__":
    main()
