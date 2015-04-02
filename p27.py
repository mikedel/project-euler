from math import sqrt

LIMIT = 1001

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

max_a = LIMIT
max_b = LIMIT
max_n = 0

for a in range(-LIMIT, LIMIT):
    for b in range(-LIMIT, LIMIT):
        n = 0
        while check_prime(n*n + a*n + b):
            n += 1
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b

print max_a * max_b
