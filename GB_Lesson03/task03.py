# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    # return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)   # используя функцию min
    if arg1 >= arg2:
        if arg2 >= arg3:
            summary = arg1 + arg2
        else:
            summary = arg1 + arg3
    elif arg1 >= arg3:
        summary = arg1 + arg2
    else:
        summary = arg2 + arg3
    return summary


x = float(input('Введите действительное число'))
y = float(input('Введите действительное число'))
z = float(input('Введите действительное число'))
print(my_func(x, y, z))
