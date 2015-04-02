LIMIT = 1001

max_y = 501
max_x = 501
min_y = 500
min_x = 500

x = 501
y = 501
current = 1
total = 1

matrix = [[0 for i in range(LIMIT+1)] for i in range(LIMIT+1)]

matrix[y][x] = current
while current < LIMIT*LIMIT:
    while x <= max_x:
        # print ' '.join(['current:', str(current), 'x:', str(x), 'y:', str(y)])
        x += 1
        matrix[y][x] = current
        current += 1
    max_x = x
    if x < LIMIT:
        total += current
    while y  <= max_y:
        # print ' '.join(['current:', str(current), 'x:', str(x), 'y:', str(y)])
        y += 1
        matrix[y][x] = current
        current += 1
    max_y = y
    if y < LIMIT:
        total += current
    while x >= min_x:
        # print ' '.join(['current:', str(current), 'x:', str(x), 'y:', str(y)])
        x -= 1
        matrix[y][x] = current
        current += 1
    min_x = x
    if x < LIMIT:
        total += current
    while y >= min_y:
        # print ' '.join(['current:', str(current), 'x:', str(x), 'y:', str(y)])
        y -= 1
        matrix[y][x] = current
        current += 1
    min_y = y
    if x < LIMIT:
        total += current

print total
