import math

class Punkt2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.odleglosc = math.sqrt(x**2 + y**2)

    def __add__(self, drugi):
        return Punkt2d(self.x + drugi.x, self.y + drugi.y)

    def __lt__(self, drugi):
        return self.odleglosc < drugi.odleglosc

    def __eq__(self, drugi):
        return self.x == drugi.x and self.y == drugi.y

    def __len__(self):
        return int(round(self.odleglosc, 0))
p1 = Punkt2d(3, 4)
p2 = Punkt2d(5, 6)
p3 = p1 + p2
print(p3.x)
print(p3.y)
print(p1 < p2)
print(p1.odleglosc)
print(p2.odleglosc)
print(p1 == p2)
print(len(p3))