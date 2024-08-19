class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        lst = list(range(1, new_floor+1))
        for i in lst:
            if new_floor < self.number_of_floors + 1 and new_floor > 0:
                print(i)

            else:
                print("Такого этажа не существует")
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
