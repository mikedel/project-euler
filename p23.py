def is_abundant(num):
    return True if sum((n for n in range(1, num/2+1) if num % n == 0)) > num else False

abundants = sorted([i for i in range(1, 28125) if is_abundant(i)])
abundants_set = set(abundants)
def is_sum(num):
    for i in abundants:
        if i > num:
            return False
        if (num - i) in abundants_set:
            return True
    return False
not_sums = [i for i in range(1, 28125) if not is_sum(i)]
print sum(not_sums)
