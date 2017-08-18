numbers = []
for b in range(1000001):
    numbers.append(1)

biggest = 0
i = 1000000
count = 0

while i > 0:
    if numbers[i] != -1:
        num = i
        while num > 1:
            if num % 2 == 0:
                num /= 2
                numbers[i] += 1
            else:
                num *= 3
                num += 1
                numbers[i] += 1
            if num < 1000000 and numbers[int(num)] > 1 :
                numbers[i] += (numbers[int(num)] - 1)
                numbers[int(num)] = -1
    i -= 1

for a in numbers:
    if a > biggest:
        biggest = a

print(a)
