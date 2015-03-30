from datetime import date
days = [date(y, m, 1) for y in range(1901, 2001) for m in range(1, 13)]
count = 0
for day in days:
    if day.weekday() == 6:
        count += 1
print count
