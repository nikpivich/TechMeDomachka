class Auto:

    def __init__(self, brand: str, age: int, mark: str, color: str = None, weight: int = None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return 'move'

    def stop(self):
        return 'stop'

    def birthday(self):
        self.age += 1
        return self.age


a = Auto('VW', 20, 'Passat', 'black', 2000)
print(a.birthday())
