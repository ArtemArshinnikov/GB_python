# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, year, city, email, phone):
    return ' '.join(
        ['Имя: ' + name, 'Фамилия: ' + surname, 'Год рождения: ' + year, 'Город проживания: ' + city, 'email: ' + email,
         'Телефон: ' + phone])


print(user_data(name='Artem', surname='Arshinnikov', year='1995', city='Moscow', email='example@mail.ru',
                phone='8-999-999-99-99'))
