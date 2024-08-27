class Animal: # Животное
    alive = True # Живой
    fed = False # Ненакормленный

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible == Plant.edible:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False
        else:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True

class Plant: # Растение
    def __init__(self, name):
        self.name = name
    edible = False # Не сьедобное


class Mammal(Animal): # Млекопитающее
    pass

class Predator(Animal): # Хищник
    pass

class Flower(Plant): # Цветок
    pass

class Fruit(Plant): # Фрукт
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
