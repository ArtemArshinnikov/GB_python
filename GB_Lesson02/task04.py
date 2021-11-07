# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

input_str = input("Enter string: ")
split_list = list(filter(None, input_str.split(' ')))

for i in range(len(split_list)):
    print(f"{i+1}. - {split_list[i][0:10]}")
