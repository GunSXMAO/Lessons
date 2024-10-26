import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def deposit(self):
        for _ in range(100):
            random_money = random.randint(50, 500)
            with self.lock:
                self.balance += random_money
                print(f"Пополнение: {random_money}. Баланс: {self.balance}")
                if self.balance >= 500:
                    self.condition.notify_all()

            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_money = random.randint(50, 500)
            print(f"Запрос на {random_money}.")
            time.sleep(0.001)

            with self.lock:
                if random_money <= self.balance:
                    self.balance -= random_money
                    print(f"Снятие: {random_money}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.condition.wait()



bk = Bank()


th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))


th1.start()
th2.start()


th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
