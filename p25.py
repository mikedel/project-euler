from math import log

f1 = 1
f2 = 1
n = 1
while log(f1, 10) < 999:
    temp = f1 + f2
    f1 = f2
    f2 = temp
    n += 1
print n

