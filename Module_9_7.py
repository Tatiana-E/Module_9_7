
def is_prime(func):
    def wrapper(*arg):
        res = func(*arg)
        count = 0
        for i in range(1, res+1):
            if res%i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrapper

@is_prime
def sum_three(*arg):
    summ = sum(arg)
    return summ

result = sum_three(2, 3, 6)
print(result)