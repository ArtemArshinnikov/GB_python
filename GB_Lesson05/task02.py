# 2. Создать текстовый файл (не программно), сохранить
# в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('task02.txt', 'r')
list_str = my_file.readlines()
print(f'Количество строк в файле - {len(list_str)}')
for i in range(len(list_str)):
    print(f'Количество слов {i+1} - ой строки {len(list_str[i].split())}')
my_file.close()
