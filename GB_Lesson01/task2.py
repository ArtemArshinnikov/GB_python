# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
input_time = int(input("Введите время в секундах >>>"))
second = input_time - 60 * (input_time // 60)
minutes = input_time // 60 - 60 * ((input_time // 60) // 60)
hours = (input_time // 60) // 24 - 24 * (((input_time // 60) // 24) // 24)
print(f'{hours:02}:{minutes:02}:{second:02}')
