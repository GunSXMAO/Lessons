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
