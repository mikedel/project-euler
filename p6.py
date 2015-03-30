square_of_sum = 24502500

sum_of_squares = 0
sums = 0
for i in range(1, 101):
    sums += i
    sum_of_squares += i*i

print sums*sums - sum_of_squares