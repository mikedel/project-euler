total = 0
cur = 1
for i in range(1, 1002):
    total += cur
    cur += 2*i
cur = 1
incr = 4
for i in range(1, 1002):
    total += cur
    if i % 2 == 0:
        incr += 4
    cur += incr
total -= 1 # remove the duplicate 1s
total -= 1000000 # remove the upper right hand corner which is outside of the 1000x1000 matrix
print total
