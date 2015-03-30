f = open('p022_names.txt')
line = f.readline()
names = sorted(line.replace("\"", "").split(','))
total = 0
for i in range(0, len(names)):
    total += (i+1) * sum([ord(c)-ord('A')+1 for c in names[i]])
print total
