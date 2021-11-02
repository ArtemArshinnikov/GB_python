# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
count = int(input("Введите число >>>"))
max_number = count - 10*(count // 10)
while (count - 1) >= 0:
    if max_number < (count - 10*(count // 10)):
        max_number = (count - 10*(count // 10))
    count = count // 10
print(max_number)
