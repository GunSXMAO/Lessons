def calculate_structure_sum(args):
    total_sum = 0
    for i in args:
        if isinstance(i, (list, dict, tuple, set)):
            total_sum += calculate_structure_sum(i)
        elif isinstance(i, int):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        if isinstance(args, dict):
            total_sum += args[i]
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
