import random

class Rettangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        self.area = base * altezza

r1 = Rettangolo(random.randint(1, 100), random.randint(1, 100))
r2 = Rettangolo(random.randint(1, 100), random.randint(1, 100))

print("Rettangolo 1:")
print("Base:", r1.base)
print("Altezza:", r1.altezza)
print("Area:", r1.area)

print("\nRettangolo 2:")
print("Base:", r2.base)
print("Altezza:", r2.altezza)
print("Area:", r2.area)
