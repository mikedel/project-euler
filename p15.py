grids = {}
grids['1x1'] = 2
for i in range(2, 21):
    grids['1x' + str(i)] = grids['1x' + str(i-1)] + 1

for i in range(2, 21):
    for j in range(i, 21):
        if i == j:
            grids[str(i) + 'x' + str(j)] = 2 * grids[str(i-1) + 'x' + str(i)]
        else:
            grids[str(i) + 'x' + str(j)] = grids[str(i-1) + 'x' + str(j)] + grids[str(i) + 'x' + str(j-1)]

print grids['20x20']
