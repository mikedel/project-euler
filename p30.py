quads = []
for i in range(10000, 100000):
    string = str(i)
    sq = 0
    for c in string:
        sq += pow(int(c), 5)
    if sq == i:
        quads.append(sq)
total = 0
for q in quads:
    total += q
print total
