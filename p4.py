palindromes = []

def check_palindrome(num):
    for i in range(0, len(num)/2):
        if num[i] != num[-(1+i)]:
            return False
    return True

for i in range(100, 999):
    for j in range(100, 999):
        string = str(i*j)
        if check_palindrome(string):
            palindromes.append(string)

numbers = []
for p in palindromes:
    numbers.append(int(p))

print max(numbers)


