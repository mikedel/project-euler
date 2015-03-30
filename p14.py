def collatz(num):
    if num % 2 == 0:
        return num/2
    return 3*num + 1

def get_collatz_size(num):
    count = 1
    while num != 1:
        num = collatz(num)
        count += 1
    return count

max_length = 1
max_collatz = 1
for i in range(1, 1000000):
    if get_collatz_size(i) > max_length:
        max_length = get_collatz_size(i)
        max_collatz = i

print max_collatz
