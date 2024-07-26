immutable_var = (1, "string", True, 1.5, [1, 2, 3])
print(immutable_var)
#immutable_var[0] = 2 - произойдет ошибка, числа не изменяются
#immutable_var[1] = "apple" - произойдет ошибка, строки не изменяются
#immutable_var[2] = False - произойдет ошибка, логические данные не изменяются
#immutable_var[3] = 2.3 - произойдет ошибка, числа(дробные числа) не изменяются
immutable_var[4][0] = 4 # - список внутри кортежа, можно изменить любой элемент.
print(immutable_var)
print()
mutable_list = [1, "string", True, 1.5]
print("Было: ", mutable_list)
mutable_list[0] = "string"
mutable_list[1] = 1
mutable_list[2] = 1.5
mutable_list[3] = False
print("Стало: ", mutable_list)
