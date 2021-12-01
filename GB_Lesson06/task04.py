# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = ''

    def go(self, speed):
        self.speed = speed
        return print('Машина поехала')

    def stop(self):
        self.speed = 0
        return print('Машина остановилась')

    def turn(self, direction: str):
        self.direction = direction
        return print(f'Машина повернула {direction}')

    def show_speed(self):
        return print(f'Скорость - {self.speed}.')


class TownCar(Car):
    s_speed = 60

    def show_speed(self):
        if self.speed > self.s_speed:
            return print(f'Скорость - {self.speed}. Внимание! Превышение скорости!')
        else:
            return print(f'Скорость - {self.speed}. Скоростной режим не нарушен.')


class WorkCar(Car):
    s_speed = 40

    def show_speed(self):
        if self.speed > self.s_speed:
            return print(f'Скорость - {self.speed}. Внимание! Превышение скорости!')
        else:
            return print(f'Скорость - {self.speed}. Скоростной режим не нарушен.')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


if __name__ == '__main__':
    cars_dict = {
        (0, 'Зеленый', 'VW Jetta'): TownCar,
        (10, 'Черный', 'Porsche 911'): SportCar,
        (0, 'Красный', 'VW Polo'): WorkCar,
        (50, 'Синий', 'VW Passat'): PoliceCar,
    }

    for attr_car, type_car in cars_dict.items():
        car = type_car(*attr_car)

        print(f"Название авто {car.name}")
        print(f"Цвет авто {car.color}")
        print(f"Это авто полиции? {car.is_police}")
        print(f"Скорость авто {car.speed}")
        car.show_speed()
        car.go(30)
        car.show_speed()
        car.go(41)
        car.show_speed()
        car.go(61)
        car.show_speed()
        car.turn('влево')
        car.turn('вправо')
        car.stop()
        car.show_speed()
