sum1 = 0
total_num = 0

for i in range(101):
    sum1 += i ** 2

for i in range(101):
    total_num += i
sum2 = total_num ** 2

print(sum2 - sum1)
