from math import sqrt

def get_triangle(num):
    total = 0
    for i in range(1, num+1):
        total += i
    return total

def get_factors(num):
    factors = []
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            factors.append(i)
            if num % i != num / i:
                factors.append(num/i)
    return factors

def get_num_factors(num):
    count = 0
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            count += 1
            if num % i != num / i:
                count += 1
    return count

number = 500
while(len(get_factors(get_triangle(number))) < 500):
    number += 1

print get_triangle(number)
