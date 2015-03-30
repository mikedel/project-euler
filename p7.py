from math import sqrt

def check_prime(num):
    if num in [4, 6, 8]:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

count = 0
current = 1
while count < 10001:
    current += 1
    if check_prime(current):
        count += 1
print current
