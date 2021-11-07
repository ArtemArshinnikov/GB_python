# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
number = int(input("Enter number: "))
count_number = my_list.count(number)

if count_number == 0:
    for element in my_list:
        if number < my_list[-1]:
            my_list.append(number)
            break
        elif number > element:
            index_element = my_list.index(element)
            my_list.insert(index_element, number)
            break
else:
    index_number = my_list.index(number)
    my_list.insert(index_number + count_number, number)
print(my_list)
