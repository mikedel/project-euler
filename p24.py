def get_digit(word, goal, part, current):
    smallest = current
    for i in range(0, len(word)):
        largest = smallest + part
        if largest >= goal:
            string = word[i]
            word = word.replace(word[i], '')
            if len(word) == 0:
                return string
            return string + get_digit(word, goal, part/(len(word)), smallest)
        else:
            smallest = largest

print get_digit('0123456789', 1000000, 362880, 0)

