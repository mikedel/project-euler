from math import sqrt

def check_prime(num):
    if num in [4, 6, 8]:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

total = 0
for i in range(2, 2000000):
    if check_prime(i):
        total += i

print total