# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

count = int(input('Enter number of list element'))
my_list = []

for i in range(count):
    my_list.append(input(f'Enter {i + 1} list element'))

if count % 2 == 0:
    i = 0
    while i < count:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
else:
    i = 0
    while i + 1 < count:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2

print(my_list)
