# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который
# результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
a = int(input("Введите результат первого дня a = >>>"))
b = int(input("Введите интересующий результат b = >>>"))
train_result = a
count = 1
while train_result < b:
    #    print(f"{count}-й день: {round(train_result, 2)}")
    count = count + 1
    train_result = train_result * 1.1
# print(f"на {count}-й день спортсмен достиг результата - не менее {b} км.")
print(count)
