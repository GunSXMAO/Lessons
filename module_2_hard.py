n = int(input("Введите первое число: "))
result = []
for j in range(1, 21):
    for k in range(1, 21):
        i = j + k
        if j == k:
            continue
        if n % i == 0:
            result.append(j)
            result.append(k)
lst = len(result)//2
for i in range(lst):
    result.pop()
for x in result:
   print(x, end='')
