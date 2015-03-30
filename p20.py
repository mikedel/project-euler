total = 1
for i in range(1, 101):
    total *= i
counter = 0
for c in str(total):
    counter += int(c)
print counter
