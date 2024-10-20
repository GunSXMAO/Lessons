import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name # Имя рыцаря
        self.power = power # Сила рыцаря
        self.enemies = 100 # Враги
        self.days = 0 # Счетчик дней битвы

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.days += 1
            if self.enemies < 0:
                self.enemies = 0
            day = 'дня' if self.days % 10 == 1 and self.days % 100 != 11 else "дней"
            print(f"{self.name}, сражается {self.days} {day}..., осталось {self.enemies} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} {day}!")

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

# Вывод строки об окончании сражения
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
