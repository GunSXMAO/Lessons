### Словари ###

my_dict = {'Ivan': 1992, 'Sasha': 1990, 'Dasha': 1996}
print('Список: ', my_dict)
print('Год рождения Ивана: ', my_dict['Ivan'])
print('Поиск несуществующего ключа: ', my_dict.get('Denis', 'Нет такого ключа!'))
my_dict.update({'Oleg': 1986,
                'Olga': 1981})
print('Обновленный список: ', my_dict)
Name = my_dict.pop('Ivan')
print('Вывод значения переменной Name: ', Name)
print('Пару Иван убрали в переменную: ', my_dict)
print()

### Множества ###

my_set = {1, 3, 4, 1, 'Sasha', 'Alex', (1, 3, 4), 'Alex', (1, 3, 4), 2, 5, 3}
print(my_set)
my_set.add(77)
my_set.add('Denis')
print(my_set)
my_set.remove('Alex')
print(my_set)
