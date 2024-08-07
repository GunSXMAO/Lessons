target_number = int(input("Введите число от 3 до 20: "))
numbers_range = range(1, 21)  # числа от 1 до 20

# Находим все уникальные пары чисел, сумма которых кратна target_number
valid_pairs = []
for i in numbers_range:
    for j in numbers_range:
        if i != j:
            if target_number % (i + j) == 0:
                pair = (i, j)
                if pair not in valid_pairs and (j, i) not in valid_pairs:
                    valid_pairs.append(pair)

# Выводим найденные уникальные пары
print(f"Уникальные пары чисел от 1 до 20, сумма которых кратна {target_number}:")

print(valid_pairs)
