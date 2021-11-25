# -*- coding: utf-8 -*-
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    dist = 0.005

    def __init__(self, arg_length, arg_width):
        self.length = float(arg_length)
        self.width = float(arg_width)

    def asphalt_mass(self, arg_thickness):
        thickness = float(arg_thickness)
        try:
            return (self.length * self.width
                    * thickness * self.dist)
        except TypeError:
            return None


if __name__ == "__main__":
    road = Road(5000, 20)
    print(f'Масса асфальта - {road.asphalt_mass(25)} тонн')
