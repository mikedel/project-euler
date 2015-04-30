quads = []
for i in range(2, 1000000):
    string = str(i)
    sq = 0
    for c in string:
        sq += pow(int(c), 5)
    if sq == i:
        print i
        quads.append(sq)
total = 0
for q in quads:
    print q
    total += q
print total
