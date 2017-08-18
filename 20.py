summ = 0
number = [1]
for i in range(2, 101):
    for x in range(len(number)):
        number[x] *= i
    count = 0
    for n in number:
        count += 1
        if n >= 10:
            if count == len(number):
                number.append(int(n/10))
            else:
                number[count] += int(n/10)
            number[count - 1] %= 10
    while number[len(number) - 1] >= 10:
        number.append(int(number[len(number) - 1] / 10))
        number[len(number) - 2] %= 10

for n in number:
    summ += n

print(summ)

