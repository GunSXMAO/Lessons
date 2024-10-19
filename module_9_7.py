def is_prime(func):
    def wrapper(*args, **kwargs):
        result_ = func(*args, **kwargs)
        if result_ <= 1:
            print('Ошибка: число должно быть больше 1')
            return result_
        for i in range(2, int(result_ ** 0.5) + 1):
            if result_ % i == 0:
                print('Составное')
                return result_
        print('Простое')
        return result_
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 4, 6)
print(result)
