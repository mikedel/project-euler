from decimal import *

sizes = {}
PRECISION = 10000
getcontext().prec = PRECISION + 2
max_size = -1
max_num = -1

for i in range(1, 1001):
    fraction = str(1/Decimal(i))[2:-1]
    for j in range(1, PRECISION):
        part = fraction[-j:]
        if part == fraction[j*-2:-j] and part == fraction[j*-3:j*-2]:
            break
    if len(part) > max_size and len(part) < PRECISION - 1:
        max_size = len(part)
        max_num = i

print ' '.join(['number:', str(max_num), 'size:', str(max_size)])
