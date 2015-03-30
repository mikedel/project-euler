from math import sqrt

def check_prime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True

number = 600851475143
current = int(sqrt(number)) + 1
for current in reversed(range(3, current, 2)):
    if number % current != 0:
        current -= 2
    elif check_prime(current):
        print current
        break
