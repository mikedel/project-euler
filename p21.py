def d(num):
    return sum([n for n in range(1, num/2 + 1) if num % n == 0])

results = []
for i in range(1, 10000):
    results.append({'d': d(i), 'num': i})

amicable_numbers = []
for i in results:
    for j in results:
        if i != j and i['d'] == j['num'] and i['num'] == j['d']:
            amicable_numbers.append(i['num'])
print amicable_numbers
print sum(amicable_numbers)
