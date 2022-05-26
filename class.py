import time


class Auto:

    def __init__(self, brand: str, age: int, mark: str, color: str = None, weight: int = None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return 'move'

    @staticmethod
    def stop():
        return 'stop'

    def birthday(self):
        self.age += 1
        return self.age


class Truck(Auto):

    def __init__(self, max_load: int, brand: str, age: int, mark: str):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        print('move')

    @staticmethod
    def load():
        time.sleep(1)
        print('time')
        time.sleep(1)


class Car(Auto):

    def __init__(self, max_speed: int, brand: str, age: int, mark: str):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        print('move')
        print(f'max speed is {self.max_speed}')


a = Auto('VW', 20, 'Passat', 'black', 2000)
b = Truck(1500, 'VW', 20, 'Passat', )
c = Car(222, 'Audi', 12, 'A8', )

b.move()
b.load()
c.move()
