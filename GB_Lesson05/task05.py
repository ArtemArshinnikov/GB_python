# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_file = open('task05.txt', 'w+')
num_line = input('Введите цифры через пробел: ')
my_file.writelines(num_line)
num_list = num_line.split()
try:
    print(sum(map(float, num_list)))
except ValueError:
    print('Неправильно набран номер. Введите число.')
