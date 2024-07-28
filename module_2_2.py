first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))
if first == second == third:
    print("У вас 3 равных числа")
elif first == second or second == third or first == third:
    print("У вас 2 одинаковых числа")
else:
    print("У вас 0 одинаковых чисел")
