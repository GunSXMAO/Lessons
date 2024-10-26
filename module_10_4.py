import threading
import random
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None     # Гость за столом (по умолчанию None)

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name # Имя гостя
    def run(self):
        time.sleep(random.randint(3, 10)) # Ожидание случайным образом от 3 до 10 секунд


class Cafe:
    def __init__(self, *tables):
        self.tables = tables  # Список столов
        self.queue = Queue()  # Очередь гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest is None: # Если стол свободен, сажаем гостя
                    free_table = table
                    break
            if free_table:
                free_table.guest = guest # Сажаем гостя
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest) # Если свободных столов нет, добавляем в очередь
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables): # Обслуживание гостей, пока есть очередь или хотя бы один стол занят
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty(): # Проверяем, есть ли очередной гость
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        next_guest.start()
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            time.sleep(1)

tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
