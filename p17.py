names = {'1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '20': 'twenty',
        '30': 'thirty',
        '40': 'forty',
        '50': 'fifty',
        '60': 'sixty',
        '70': 'seventy',
        '80': 'eighty',
        '90': 'ninety',
        '100': 'hundred',
        '1000': 'thousand',
        'and': 'and'
        }
values = {}
for k, v in names.iteritems():
    values[k] = len(v)

counter = 0
for i in range(1, 1000):
    count = 0
    if i >= 100:
        count += values['100']
        count += values[str(i/100)]
        if i % 100 != 0:
            count += values['and']
            if i % 100 < 20:
                count += values[str(i % 100)]
            else: # larger than 100 and more than 20
                if i % 10 != 0:
                    count += values[str(i%10)]
                count += values[str(int(i%100/10)*10)]
    else:
        if i < 20:
            count += values[str(i)]
        else:
            if i % 10 != 0:
                count += values[str(i%10)]
            count += values[str(int(i/10)*10)]
    counter += count
    print ' '.join(['i:', str(i), 'count:', str(count)])

counter += values['1'] + values['1000']

print counter
