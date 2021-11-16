# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count
from itertools import cycle


def count_func(start_num, stop_num):
    for i in count(start_num):
        if i > stop_num:
            break
        else:
            print(i)


def cycle_func(enter_list, count_num):
    i = 0
    iteration = cycle(enter_list)
    while i < count_num:
        print(next(iteration))
        i += 1


count_func(int(input("Введите первый элемент списка: ")), int(input("Введите последний элемент списка: ")))
cycle_func([1, 2, 3], int(input("Введите количество выводимых элементов: ")))
