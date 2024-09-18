class Vehicle: # Автомобиль
    __COLOR_VARIANTS = ['Black', 'Red', 'Blue', 'Green', 'White', 'Orange']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner # владелец транспорта
        self.__model = model # модель (марка) транспорта
        self.__color = color # цвет транспорта
        self.__engine_power = engine_power # мощность двигателя

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'


    def set_color(self, new_color):
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")


class Sedan(Vehicle):# Седан
    __PASSENGERS_LIMIT = 5  # количество пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()