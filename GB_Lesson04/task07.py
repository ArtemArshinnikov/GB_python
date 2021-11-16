# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и
# до n!.

def fact(number):
    count = 1
    x = 1
    while count <= number:
        yield count * x
        x = count * x
        count += 1


i = 1
num_list = []
n = int(input('Введите n: '))
for el in fact(n):
    if i > n:
        break
    else:
        num_list.append(el)
        i += 1
print(num_list)
