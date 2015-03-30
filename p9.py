from math import sqrt

for a in range(1, 334):
    for b in range(a, 500):
        c = 1000 - a - b
        if c == sqrt(a*a + b*b):
            print ' '.join(['a:', str(a), 'b:', str(b), 'c:', str(c)])
            print a*b*c
            exit()