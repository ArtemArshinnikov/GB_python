# -*- coding: utf-8 -*-
# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return ' '.join(sorted([self.surname, self.name]))

    def get_total_income(self):
        return sum(self.income.values())


if __name__ == '__main__':
    personal_list = [{
            'name': 'Иван',
            'surname': 'Иванов',
            'position': 'Инженер',
            'wage':  55000,
            'bonus': 20000
        },
        {
            'name': 'Светлана',
            'surname': 'Иванова',
            'position': 'Бухгалтер',
            'wage':  40000,
            'bonus': 10000
        }]

    for item in personal_list:
        a = Position(**item)

        print(f'Имя сотрудника: {a.name};\n'
              f'Фамилия сотрудника: {a.surname};\n'
              f'Полное имя сотрудника: {a.get_full_name()};\n'
              f'Должность сотрудника: {a.position};\n'
              f'Общий доход сотрудника: {a.get_total_income()}\n\n')
