import random

from read_save import read_content, save_content

PRODUCTS_FILE_NAME = 'products.json'


def name_validation(name: str):
    if name != '':
        return name


def cost_validation(cost: str):
    if ',' in cost or '.' in cost:
        total_cost = cost.replace(',', '').replace('.', '')
    else:
        total_cost = f'{cost}00'
    if total_cost.isdigit():
        return int(total_cost)


def type_validation(product_type: str):
    match(product_type):
        case('1'): return 'грамм'
        case('2'): return 'шт'
        case('3'): return 'мл'


def size_validation(size: str):
    if size.isdigit():
        return int(size)


def generate_product_id():
    product_id = random.randint(100, 999)
    return product_id


def main():
    products_content = {}
    if content := read_content(PRODUCTS_FILE_NAME):
        products_content = content
    while True:
        product_name = input('Введите название продукта: ')
        if not name_validation(product_name):
            print('Имя продукта не может быть пустым')
            continue
        description = input('Добавте описание продукта: ')
        cost = input('Какая стоимость продукта: ')
        if not cost_validation(cost):
            print('Вы ввели не число')
            continue
        product_type = input('''Выберите единицы измерения продукта 
            1) грамм
            2) шт
            3) мл
            Ваш ответ:
        ''')
        if not type_validation(product_type):
            print('Введите 1 или 2 или 3 !!!')
            continue
        size = input('Введите количество продукта(шт/мл/грамм): ')
        if not size_validation(size):
            print('Вы ввели не число')
            continue
        valid_name = name_validation(product_name)
        valid_cost = cost_validation(cost)
        valid_type = type_validation(product_type)
        valid_size = size_validation(size)
        product_id = generate_product_id()
        products_content[product_id] = {
            'product_name': valid_name,
            'description': description,
            'cost': valid_cost,
            'type': valid_type,
            'size': valid_size,
            'on_stop_list': False
        }
        answer = input('Хотите продолжить добавлять продукты(y/n): ')
        if answer.lower() in ['n', 'no']:
            save_content(file_name=PRODUCTS_FILE_NAME, content=products_content)
            break


if __name__ == '__main__':
    main()
