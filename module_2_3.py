# Первый вариант.
my_list = [42, 2, 0, 13, 0, 99, -3, 9, 8, 7, 1, 5]
len_list = len(my_list)
counting = 0
while True:
    for new in my_list:
        if len_list < counting:
            break
        if new <= -1:
            break
        if new >= 1:
            counting = counting+1
            print(new)
        continue
    break


# Второй вариант.
my_list = [42, 2, 1, 13, 0, 99, -3, 9, 8, 7, 1, 5]
index = 0
while index < len(my_list):
    if my_list[index] == 0:
        index += 1
        continue
    elif my_list[index] <= -1:
        break
    elif my_list[index] >= 1:
        print(my_list[index])
        index += 1
        continue
