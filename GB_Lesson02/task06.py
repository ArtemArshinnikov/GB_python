'''6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}'''

product_list = []

while input('ADD PRODUCT (yes/no)?') == 'yes':
    number = input('Please enter product number')
    product_dict = {"name": input("Add product name"),
             "price": input("Add product price"),
             "count": input("Add product count"),
             "value": input("Add product value")}
    product_tuple = (number, product_dict)
    product_list.append(product_tuple)

print(product_list)

name_list = []
price_list = []
count_list = []
value_list = []

for i in range(len(product_list)):
    name_list.append(product_list[i][1]["name"])
    price_list.append(product_list[i][1]["price"])
    count_list.append(product_list[i][1]["count"])
    value_list.append(product_list[i][1]["value"])

value_list = list(set(value_list))
analitics_dict = {"name": name_list,
                  "price": price_list,
                  "count": count_list,
                  "value": value_list}
print(analitics_dict)
