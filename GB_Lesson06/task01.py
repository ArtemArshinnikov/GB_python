# -*- coding: utf-8 -*-
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    color = {'red': 7, 'yellow': 2, 'green': 6}

    def running(self):
        for signal, signal_time in self.color.items():
            print(f"TrafficLight is '{signal}' on {signal_time} seconds")
            sleep(signal_time)


if __name__ == "__main__":
    a = TrafficLight()
    a.running()
