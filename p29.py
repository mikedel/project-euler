squares = []
for a in range(2, 101):
    for b in range(2, 101):
        sq = pow(a, b)
        if sq not in squares:
            squares.append(sq)

print len(squares)
