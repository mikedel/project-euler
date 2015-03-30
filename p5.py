def evenly_divides(number):
    for i in [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]:
        if number % i != 0:
            return False
    return True

current = 2520
while not evenly_divides(current):
    current += 1

print current

