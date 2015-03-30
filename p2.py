total = 0
temp = 1
last = 1
current = 1
while(current < 4000000):
    temp = current
    current = last + current
    last = temp
    if current % 2 == 0:
        total += current

print total


