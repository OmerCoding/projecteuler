year = 1901
month = 1
day = 6
count = 0

while year < 2001:
    month = 1
    while month < 13:
        if month == 9 or month == 4 or month == 6 or month == 11:
            while day < 31:
                day += 7
            day -= 30
            if day == 1:
                count += 1
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            while day < 32:
                day += 7
            day -= 31
            if day == 1:
                count += 1
        else:
            if year % 4 == 0:
                while day < 30:
                    day += 7
                day -= 29
                if day == 1:
                    count += 1
            else:
                while day < 29:
                    day += 7
                day -= 28
                if day == 1:
                    count += 1
        month += 1
    year += 1

print(count)