# 1. Создать программно файл в текстовом формате, записать
# в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_file = open('task01.txt', 'w')
my_line = input('Введите текст \n')
while my_line:
    my_file.writelines(my_line + '\n')
    my_line = input('Введите текст \n')
    if not my_line:
        break
my_file.close()
