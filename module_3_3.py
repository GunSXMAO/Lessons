#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params() # Ошибки нет.
print_params(2, 4, 10) # Ошибки нет.
print_params("Hi", 4, "Hello") # Ошибки нет.
print_params(a = 'Hello', b = 10, c = False) # Ошибки нет.
print_params(b = 25) # Ошибки нет.
print_params(c = [1, 2, 3]) # Ошибки нет.

#2.Распаковка параметров:

values_list = [1, "string", False]
values_dict = {'a': False, 'b': 5, 'c': "string"}
print_params(*values_list) # Ошибки нет.
print_params(**values_dict) # Ошибки нет.

#3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) # Ошибки нет, работает = 54.32 Строка 42
