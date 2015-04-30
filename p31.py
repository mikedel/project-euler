def is_pandigital(string):
    if len(string) != 9:
        return False
    is_pandigital = True
    if string.find('1') == -1 or string.rfind('1') != string.find('1'):
        is_pandigital = False
    elif string.find('2') == -1 or string.rfind('2') != string.find('2'):
        is_pandigital = False
    elif string.find('3') == -1 or string.rfind('3') != string.find('3'):
        is_pandigital = False
    elif string.find('4') == -1 or string.rfind('4') != string.find('4'):
        is_pandigital = False
    elif string.find('5') == -1 or string.rfind('5') != string.find('5'):
        is_pandigital = False
    elif string.find('6') == -1 or string.rfind('6') != string.find('6'):
        is_pandigital = False
    elif string.find('7') == -1 or string.rfind('7') != string.find('7'):
        is_pandigital = False
    elif string.find('8') == -1 or string.rfind('8') != string.find('8'):
        is_pandigital = False
    elif string.find('9') == -1 or string.rfind('9') != string.find('9'):
        is_pandigital = False
    return is_pandigital


total = 0
for a in range(0, 9999):
    for b in range(0, 9999):
        c = a * b
        string = str(a) + str(b) + str(c)
        if a > b and is_pandigital(string):
            total += c
            print string
print total
