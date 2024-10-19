def apply_all_func(int_list, *functions):
    results = {}
    for num in functions:
        num_new = num(int_list)
        results[num.__name__] = num_new
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
