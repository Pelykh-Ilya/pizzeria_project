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
    price_in_uah = price / 100
    return price_in_uah


def list_of_order_product(ordered_position: list):
    order_list = []
    for item in ordered_position:
        order_list.append(product_content[item]['product_name'])
    order_str = ', '.join(order_list)
    return order_str


def generate_order_id():
    return random.randint(1, 1000)


def show_product(product_id: int):
    return f'''
        {product_content[f"{product_id}"]["product_name"]} цена {product_content[f"{product_id}"]["cost"]/100} грн
        {product_content[f"{product_id}"]["description"]} {product_content[f"{product_id}"]["size"]} {product_content[f"{product_id}"]["type"]}
    '''


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
            1 {show_product(397)}
            2 {show_product(953)}  
            3 {show_product(804)}
            4 {show_product(515)}
            5 {show_product(568)}
            6 {show_product(627)}
            Ваш выбор №: 
        ''')
        match (order):
            case ('1'): ordered_position_id.append('397')
            case ('2'): ordered_position_id.append('953')
            case ('3'): ordered_position_id.append('804')
            case ('4'): ordered_position_id.append('515')
            case ('5'): ordered_position_id.append('568')
            case ('6'): ordered_position_id.append('627')
            case _: print('Такой позиции нет в меню')
        answer = input("Желаете еще что нибудь заказать?(y/n): ")
        if answer.lower() in ['no', 'n']:
            break
    coment_to_order = input('Добавьте коментарий к заказу: ')
    total_price = return_total_price(ordered_position_id)
    order_in_str = list_of_order_product(ordered_position_id)
    check_order = input(f'''
        Ваш заказ: {order_in_str}
        Общая сумма: {total_price} грн
        Адрес доставки: дом {customers_content[customers_id]["building_num"]} квартира {customers_content[customers_id]["apartament_num"]}
        Подтверждаете(y/n): 
    ''')
    if check_order.lower() in ['yes', 'ye', 'y']:
        generated_order_id = generate_order_id()
        order_content[generated_order_id] = {
            'client': customers_content[customers_id],
            'ordered_position': order_in_str,
            'comment': coment_to_order,
            'total_cost': total_price
        }
        save_content(file_name=ORDER_FILE_NAME, content=order_content)


if __name__ == '__main__':
    main()
