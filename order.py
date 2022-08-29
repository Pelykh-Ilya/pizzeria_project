import random

from read_save import read_content, save_content

CUSTOMERS_FILE_NAME = 'customers.json'
PRODUCTS_FILE_NAME = 'products.json'
ORDER_FILE_NAME = 'order.json'

product_content = read_content(PRODUCTS_FILE_NAME)
customers_content = read_content(CUSTOMERS_FILE_NAME)


def return_total_price(ordered_position_id: list):
    price = 0
    for item in ordered_position_id:
        price += product_content[item]['cost']
    return price

def list_of_order_product(ordered_position: list):
    order_list = []
    for item in ordered_position:
        order_list.append(product_content[item]['product_name'])
    order_str = ', '.join(order_list)
    return order_str


def generate_order_id():
    return random.randint(1, 1000)


def show_product_menu(content: dict):
    i = 1
    menu = ''
    for product_id in content.keys():
        menu += f'''
        {i} {product_content[product_id]["product_name"]} цена {product_content[product_id]["cost"] / 100} грн
        {product_content[product_id]["description"]} {product_content[product_id]["size"]} {product_content[product_id]["type"]}
       
        '''
        i+= 1
    return menu
    

def main():
    while True:
        customers_id = input('Введите ваш телеграмм ID: ')
        if customers_id in customers_content:
            print(f'Добро пожалвать {customers_content[customers_id]["name"]}')
            break
        else:
            print('Неверно указан телеграмм ID')
            continue
    ordered_position_id = []
    while True:
        order_content = {}
        if content := read_content(ORDER_FILE_NAME):
            order_content = content
        order = input(f'''
            Что желаете заказать?
            {show_product_menu(product_content)}
            Ваш выбор №: 
        ''')
        list_of_key = list(product_content.keys())
        if int(order) <= len(list_of_key):
            ordered_position_id.append(list_of_key[int(order) - 1])
        else:
            print('Такой позиции нет в меню')
        answer = input("Желаете еще что нибудь заказать?(y/n): ")
        if answer.lower() in ['no', 'n']:
            break
        else:
            continue
    coment_to_order = input('Добавьте коментарий к заказу: ')
    total_price = return_total_price(ordered_position_id)
    order_in_str = list_of_order_product(ordered_position_id)
    check_order = input(f'''
        Ваш заказ: {order_in_str}
        Общая сумма: {total_price / 100} грн
        Адрес доставки: дом {customers_content[customers_id]["building_num"]} квартира {customers_content[customers_id]["apartament_num"]}
        Коментарий: {coment_to_order}
        Подтверждаете(y/n): 
    ''')
    if check_order.lower() in ['yes', 'ye', 'y']:
        generated_order_id = generate_order_id()
        order_content[generated_order_id] = {
            'client': customers_content[customers_id],
            'ordered_position': ordered_position_id,
            'comment': coment_to_order,
            'total_cost': total_price
        }
    save_content(file_name=ORDER_FILE_NAME, content=order_content)


if __name__ == '__main__':
    main()
